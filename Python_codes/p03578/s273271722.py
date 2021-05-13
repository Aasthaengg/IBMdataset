import collections
n = int(input())
d = list(map(int,input().split()))
dc = collections.Counter(d)

m = int(input())
t = list(map(int,input().split()))
dt = collections.Counter(t)

for k,v in dt.items():
    if dc[k] < v:
        print("NO")
        exit()

print("YES")