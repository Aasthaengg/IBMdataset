def s(k):
    return k*(k+1)//2

n = int(input())
ans = 0

for i in range(1, n+1):
    ans += i * s(n//i)
print(ans)
