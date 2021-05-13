N = int(input())
S, T = map(list, input().split())

ans = ""
for i in range(N):
    ans = ans + S[i] + T[i]

print(ans)