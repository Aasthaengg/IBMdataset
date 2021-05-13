n = int(input())
k = int(input())
ans = 1
for _ in range(n):
    a = ans*2
    b = ans + k
    ans = min(a,b)

print(ans)