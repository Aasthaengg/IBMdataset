h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
b=[0]*26
for aa in a:
  for ai in aa:
    b[ord(ai)-97]+=1

x=(h//2)*(w//2)
y=(h%2)*(w//2)+(h//2)*(w%2)
z=(h%2)*(w%2)

for bb in b:
  t=bb
  while x and t>3:
    x-=1
    t-=4
  while y and t>1:
    y-=1
    t-=2
  z-=t
if not(x==y==z==0):
  print("No")
else:
  print("Yes")