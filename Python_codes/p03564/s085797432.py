N = int(input())
K = int(input())
n = 1
for _ in range(N):
    if n*2 <= n+K:
        n = n*2
    else:
        n = n + K
    
print(n)