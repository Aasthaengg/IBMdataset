n=int(input())
a=list(map(int,input().split()))
mean = sum(a)/n
ans = -1
sa= 1234567890
for i in range(n):
    if sa > abs(mean - a[i]):
        ans = i 
        sa = abs(mean - a[i])
print(ans)