n=int(input())
p=list(map(int,input().split()))
count=0
num=[]

for i in range(1,n-1):
  num.append([p[i-1],p[i],p[i+1]])

for i in num:
  a=i[1]
  i.sort()
  if i[1]==a:
    count+=1
    
print(count)