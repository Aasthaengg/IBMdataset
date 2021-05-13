n=int(input())
a=[int(input()) for _ in range(n)]
b=sorted(a)
if b[-1]==b[-2]:f=1
else:f=0
for i in a:
  if f:print(b[-1])
  else:
    if i==b[-1]:print(b[-2])
    else:print(b[-1])