import collections

n=int(input())
d=list(map(int,input().split()))
d=collections.Counter(d)
m=int(input())
t=list(map(int,input().split()))
t=collections.Counter(t)


for i in t:
    if t[i]>d[i]:
        print("NO")
        exit()
print("YES")