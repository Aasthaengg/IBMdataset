from collections import Counter
h,w=map(int,input().split())
s=""
for i in range(h):
  s+=input()
sc=Counter(s)
d=[0,0,0]
for v in sc.values():
    d[0]+=(v//4)*4
    d[1]+=2 if v%4>=2 else 0
    d[2]+=v%2

if w%2==0 and h%2==0:
  print("Yes" if d[0]==h*w else "No")
elif (w%2)*(h%2)==1:
  print("Yes" if d[1]<=(w-1)+(h-1) and d[2]==1 else "No")
elif w%2==0:
  print("Yes" if d[1]<=w and d[2]==0 else "No")
elif h%2==0:
  print("Yes" if d[1]<=h and d[2]==0 else "No")

