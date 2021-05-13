n = int(input())

ans = 0

for i in range(1,n+1):
    a = n//i
    b = i*a

    ans += (i+b)*a//2

print(ans)
