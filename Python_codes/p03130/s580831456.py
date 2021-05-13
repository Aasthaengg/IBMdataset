r=[]
for i in range(3):
  a,b=map(int,input().split())
  r.append(a);r.append(b)
print("YES" if r.count(1) <=2 and r.count(2) <=2 and r.count(3)<=2 and r.count(4) <=2 else "NO")
