n=int(input())
rb=[]
for i in range(n):
  x,l=map(int,input().split())
  rb.append((x,l))
rb.sort()

d=[1,sum(rb[0])]
for i in range(1,len(rb)):
  if sum(rb[i])<d[1]:
    d[1]=sum(rb[i])
  elif rb[i][0]-rb[i][1]>=d[1]:
    d[0]+=1
    d[1]=sum(rb[i])
print(d[0])