n,l = map(int,input().split())
small = 1000
sum = 0
for i in range(1,n+1):
    sum = sum + l + i - 1
    if abs(l+i-1) <= small:
        small = abs(l+i-1)
        
if sum > 0:
    print(sum-small)
else:
    print(sum+small)