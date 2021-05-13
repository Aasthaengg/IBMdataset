N,A,B,C=map(int,input().split())
l=[int(input()) for i in range(N)]
D=0
a=0
b=0
c=0
mp=10**5
#4^8=2^16=10^16*0.3010=10^5?
for i in range(4**N):
  a=0
  b=0
  c=0
  x=0
  y=0
  z=0
  for j in range(N):
    if(i&1<<2*j and i&1<<(2*j+1)):
      #A-=[l[j]
      a+=l[j]
      x+=1
    elif(i&1<<2*j and ~(i&1<<(2*j+1))):
      b+=l[j]
      y+=1
    elif(~(i&1<<2*j) and (i&1<<(2*j+1))):
      c+=l[j]
      z+=1
  if(a==0 or b==0 or c==0):
    continue

  mp=min(mp,abs(A-a)+abs(B-b)+abs(C-c)+(x+y+z-3)*10)
  if(mp==110):
    print("a={}".format(a)+"b={}".format(b)+"c={}".format(c))
print(mp)