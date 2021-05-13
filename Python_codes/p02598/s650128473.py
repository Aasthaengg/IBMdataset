import math

N,K = map(int,input().split())

a = list(map(int, input().split()))
l = 0
r = max(a)

x = (l+r)//2
ans = r+1
while(r>1+l):

    
    x = (l+r)//2
    if x == 0:
        break

    count = 0
    for i in range(N):
        count += math.ceil(a[i] /x)-1
    if (count <=K):
        if (ans > x):
            ans = x
        r = x
    else:
        l = x
count = 0
ans = x
if(x!= 0 and l != 0):
        
    for i in range(N):
        count += math.ceil(a[i]/l)-1

    if (count <=K):
        ans = l
    else:
        ans = r

if l==0:
    ans = r
print(ans)

        
        

    
