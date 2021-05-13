import sys
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = []
for i in range(0,n-1):
    if(a[i]==a[i+1]):
        ans.append(a[i])
if len(ans) <2:
    print(0)
    sys.exit()
        
if (ans[0]==ans[1] and ans[1]!=ans[2]):
    print(ans[0]*ans[2])
    sys.exit()

print(ans[0]*ans[1])