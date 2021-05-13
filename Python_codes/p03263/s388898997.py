h,w=map(int,input().split())
m=[]
for i in range(h):
  m.append(list(map(int,input().split())))

ans=[]
for i in range(h-1):
  for j in range(w):
    if m[i][j]%2:
      ans.append(" ".join(map(str,(i+1,j+1,i+2,j+1))))
      m[i+1][j]+=1
for j in range(w-1):
  if m[h-1][j]%2:
    ans.append(" ".join(map(str,(h,j+1,h,j+2))))
    m[h-1][j+1]+=1

print(len(ans))
print("\n".join(ans))