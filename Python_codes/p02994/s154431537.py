num = 0
n,l = map(int, input().split())
if l <= 0 < l+n-1:
    for i in range(1,n+1):
        num += (l+i-1)
elif l > 0:
    for i in range(2,n+1):
        num += (l+i-1)
else:
    for i in range(1,n):
        num += (l+i-1)
print(num)