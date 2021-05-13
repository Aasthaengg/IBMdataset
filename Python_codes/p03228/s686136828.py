a,b,k=map(int,input().split())
t=1
for _ in range(k):
  if t:
    t=0
    a//=2
    b+=a
  else:
    t=1
    b//=2
    a+=b
print(a,b)