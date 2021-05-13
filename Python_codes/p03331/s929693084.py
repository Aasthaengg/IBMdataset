N = int(input())

def f(n):
    n = str(n)
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    return res

ans = 1000000
for i in range(1, N//2+1):
    ans = min(ans, f(i)+f(N-i))
print(ans)