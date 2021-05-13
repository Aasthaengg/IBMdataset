a,b,k=map(int,input().split())
turn="T"
for i in range(k):
  if turn=="T":
    b+=a//2
    a//=2
    turn="A"
  else:
    a+=b//2
    b//=2
    turn="T"
print(a,b)
