from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline()).split())

n,m=nii()

list=[[] for i in range(n+1)]

for i in range(m):
  p,y=nii()
  list[p].append([y,i])

ans=[]
for i in range(1,n+1):
  tl=list[i]
  s_tl=sorted(tl,key=lambda x:x[0])
  for j in range(len(tl)):
    town=s_tl[j][1]
    s1=str(i).zfill(6)
    s2=str(j+1).zfill(6)
    s=s1+s2
    ans.append([town,s])

ans.sort(key=lambda x:x[0])
for i,j in ans:
  print(j)