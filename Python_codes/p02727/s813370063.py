x,y,A,B,C = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = list(map(int, input().split()))
aa = a[len(a)-x:]
bb = b[len(b)-y:]
for i in aa:
  c.append(i)
for i in bb:
  c.append(i)
c = sorted(c)
cc = c[len(c)-x-y:]
print(sum(cc))