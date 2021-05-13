import collections
 
n = int(input())
d = sorted(list(map(int,input().split())))
m = int(input())
t = list(map(int,input().split()))

cd = collections.Counter(d)
ct = collections.Counter(t)

flg = True
for k in ct.items():
  if k[1] > cd[k[0]]:
    flg = False

print('YES' if flg else 'NO')