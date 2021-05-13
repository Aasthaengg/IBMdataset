n=int(input())
v=[int(x) for x in input().split()]
v.sort()
while len(v)!=1:
  a=v.pop(0)
  b=v.pop(0)
  v.append((a+b)/2)
  v.sort()
print(v[0])