N=int(input())
x=[0]*N
y=[0]*N
h=[0]*N
t=[0]*N
for i in range(N):
  x[i],y[i],h[i]=map(int,input().split())
  t[i]=[x[i],y[i],h[i]]

t.sort(key=lambda x:x[2],reverse=True)

for i in range(101):
  for j in range(101):
    ans=[]
    for k in t:
      d = abs(k[0]-i)+ abs(k[1]-j)
      h_tmp = d + k[2]
      if ans==[]:
        ans.append(k+[d,h_tmp])
      else:
        if d>ans[-1][-1] and k[2]==0:
          pass
        else:
          if h_tmp!=ans[-1][-1]:
            break
    else:
      print(i,j,ans[-1][-1])
      exit()
