import fractions

N, M = map(int, input().split())
S = input()
T = input()

# 最小公倍数を求める
l = (N * M) // fractions.gcd(N, M)

ans = {1: S[0]}
for i in range(1, N):
    c_num = i*l//N+1
    ans[c_num] = S[i]

for i in range(M):
    if i == 1:
        if ans[1] != T[0]:
            print(-1)
            exit(0)

    c_num = i*l//M+1
    if c_num in ans:
        if ans[c_num] != T[i]:
            print(-1)
            exit(0)
    else:
        ans[c_num] = T[i]
print(l)
