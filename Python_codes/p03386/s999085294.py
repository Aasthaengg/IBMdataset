a,b,k = map(int,input().split())

ans = []
for i in range(k):
    x = a+i
    if (x not in ans) and x<=b: 
        ans.append(x)
for j in range(k,0,-1):
    x = b-j+1
    if (x not in ans) and x>=a:
        ans.append(x)
print('\n'.join(map(str,ans)))