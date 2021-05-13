import collections
n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))

d=collections.Counter(d)
t=collections.Counter(t)
#print(d)
#print(t)
for i in t.keys():
    if d[i]<t[i]:
        print("NO")
        break
else:
    print("YES")
