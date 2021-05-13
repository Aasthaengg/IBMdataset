N, M, X = map(int, input().split())
A = list(map(int, input().split()))

#~ゴール
cnt_g = 0
for i in range(X+1, N):
    if i in A: cnt_g+= 1

#~スタート
cnt_s = 0
for i in range(X-1, 0, -1):
    if i in A: cnt_s += 1

print(min(cnt_g, cnt_s))