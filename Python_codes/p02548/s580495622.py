n = int(input())

ans = 0

for i in range(1,n):
    s = (n-1)//i
    if  0< s < n:
        ans += s
print(ans)