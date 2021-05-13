N, K, Q = map(int, input().split())
# 全問不正解の場合を初期値にする
l = [K - Q] * N
# 正解者に１ポイント加算
for _ in range(Q):
    A = int(input())
    l[A - 1] += 1

for li in l:
    if li <= 0:
        print("No")
    else:
        print("Yes")
