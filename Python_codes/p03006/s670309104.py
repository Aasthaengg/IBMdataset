n=int(input())
l=[]
if n==1:
  print(1)
else:
  for i in range(n):
    x,y=map(int,input().split())
    l.append([x,y])

  dic={}
  for i in range(n):
    for j in range(n):
      if i==j:
        continue
      dx,dy = l[j][0]-l[i][0],l[j][1]-l[i][1]
      if (dx,dy) not in dic:
        dic[dx,dy]=1
      else:
        dic[dx,dy]+=1

  dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
  print(n-dic[0][1])
