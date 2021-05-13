import sys
n = int(input())
l = list(map(int,input().split()))
if n==2:
    ans = l[0]*2
    print(ans)
    sys.exit()
    
ans = 0
lis = []
a,b = l[0],l[1]
if a<=b:
    ans +=a
    lis.append(a)
else:
    ans += a
    lis.append(b)
    
for i in range(n-2):
    a,b = l[i],l[i+1]
    if a<=b:
        ans += a
        lis.append(a)
    else:
        ans += b
        lis.append(b)
        
ans += l[n-2]
print(ans)