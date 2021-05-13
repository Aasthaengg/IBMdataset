import collections
n = int(input())
a = sorted(list(map(int,input().split())))
b = set(a)
c = collections.Counter(a)
x = 0
for i in b:
    if c[i]%2==0:x+=1
ans = len(b)
if x%2==1:ans-=1
print(ans)