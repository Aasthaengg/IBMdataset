C=[0]*4
for i in range(3):
  a,b=map(int,input().split())
  C[a-1]+=1
  C[b-1]+=1
print("YES" if C.count(1)==2 and C.count(2)==2 else "NO")