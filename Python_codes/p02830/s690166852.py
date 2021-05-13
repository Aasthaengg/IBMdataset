N = int(input())
S, T = input().split()
S = list(S)
T = list(T)
ans = ""
for i in range(N):
    ans += S[i]
    ans += T[i]
print(ans)
