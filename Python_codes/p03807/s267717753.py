from collections import Counter

n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]%=2
c=Counter(a)
if c[1]%2==1:
    print("NO")
else:
    print("YES")
