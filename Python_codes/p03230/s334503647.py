n=int(input())
num = 8*n+1
import math
a=int(math.sqrt(num))
ok=False
for i in [a-2,a-1,a,a+1,a+2]:
    if i**2 == num:
        ok=True
if not ok:
    print("No")
    exit()
print("Yes")
k=1+(a-1)//2
print(k)

from collections import defaultdict
ans=defaultdict(list)

i=0
j=1
for now in range(1,n+1):
    ans[i].append(now)
    ans[j].append(now)
    j+=1
    if j==k:
        i+=1
        j=i+1
        if i==k:
            break

for lis in ans.values():
    print(k-1,end=" ")
    print(*lis)