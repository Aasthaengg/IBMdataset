N = int(input())

def f(n):
    ans = 0
    for s in str(n):
        ans += int(s)
    return ans

ans = float("INF")
for i in range(1, N):
    j = N-i
    ans = min(ans, f(i) + f(j))
    
print(ans)