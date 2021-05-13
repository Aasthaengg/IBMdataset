n=int(input())
lst=[list(map(int,input().split())) for i in range(n)]
lst=[[i[0]-i[1],i[0]+i[1]] for i in lst]

lst.sort(key=lambda x:x[1])

pin=lst[0][1]
ans=1

for i in range(1,n):
  if pin<=lst[i][0]:
    ans+=1
    pin=lst[i][1]

print(ans)