from collections import Counter
n=int(input())
d=Counter(list(map(int,input().split())))
m=int(input())
t=list(map(int,input().split()))
for i in t:
 if d[i]==0:print("NO");exit()
 else:d[i]-=1
print("YES")