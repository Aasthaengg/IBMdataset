q=int(input())
lr=[]
for i in range(q):
  lr.append(list(map(int,input().split())))

p=[]
for i in range(2,100001):
  f=1
  for j in p:
    if j>i**0.5:
      break
    if i%j==0:
      f=0
      break
  if f:
    p.append(i)
p.append(10000000000)
s=[0]
j=0
k=0
for i in range(1,100001,2):
  if p[j]<i:
    j+=1
  if p[k]<(i+1)//2:
    k+=1
  if (i==p[j])and((i+1)//2==p[k]):
    s.append(s[-1]+1)
  else:
    s.append(s[-1])
  s.append(s[-1])

for i in lr:
  print(s[i[1]]-s[i[0]-1])