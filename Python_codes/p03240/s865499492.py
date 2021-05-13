n=int(input())
data=[list(map(int,input().split())) for i in range(n)]
data.sort(key=lambda x:x[2],reverse=True)
def cal(y,x,datum,height):
  return max(height-(abs(y-datum[1])+abs(x-datum[0])),0)==datum[2]
for i in range(101):
  for j in range(101):
    height=abs(i-data[0][1])+abs(j-data[0][0])+data[0][2]
    flag=0
    for k in data[1:]:
      if not cal(i,j,k,height):
        flag=1
        break
    if flag:pass
    else:print(j,i,height);exit()
