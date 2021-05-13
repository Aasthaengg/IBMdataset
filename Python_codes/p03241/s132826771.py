N, M = map(int, input().split())
ans = 1
K = M//N
for i in range(1, int(M**0.5)+1):
    if M%i == 0:
        if i <= K:
            ans = max(ans, i)
        if M//i <= K:
            ans = max(ans, M//i)

print(ans)