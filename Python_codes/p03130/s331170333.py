L=[0]*5
for i in range(3):
  a,b=map(int,input().split())
  L[a]+=1
  L[b]+=1
#print(L)

print("NO" if max(L)==3 else "YES")