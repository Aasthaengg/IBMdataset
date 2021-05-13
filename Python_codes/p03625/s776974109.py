from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))

b= defaultdict(int)
ans = []
ans2 = []
for i in range(n):
    b[a[i]] += 1
    if b[a[i]] == 2:
       ans.append(a[i])
    if b[a[i]] == 4:
        ans2.append(a[i])
ans = sorted(ans,reverse=True)
ans2 = sorted(ans2,reverse=True)
if len(ans) <= 1 and len(ans2) == 0:
    print(0)
    exit()
if len(ans2) == 0:
    print(ans[0]*ans[1])
elif len(ans) <= 1:
    print(ans2[0]**2)
else:
    print(max(ans[0]*ans[1],ans2[0]**2))