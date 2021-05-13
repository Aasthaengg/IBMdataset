N,M = map(int, input().split())

if M >= 2*N:
    ans = N
    M -= 2*N
    ans += M//4
else:
    ans = M//2
print(ans)