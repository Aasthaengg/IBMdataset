n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
#増えるとしたら1,2,3..のように増加分は1ずつ
#減るとしたらnumになるとして、一つ前をnum-1にする!
if l[0]!=0:
  print(-1)
  exit()
ans=0
now=0
for i in range(1,n):
  if l[i]==1+now:
    now+=1
    ans+=1
  elif l[i]>now:
    print(-1)
    exit()
  else:
    now=l[i]
    ans+=l[i]
print(ans)