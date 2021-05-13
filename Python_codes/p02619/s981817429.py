d=int(input())
a=[]
for x in range(d+1):
  b=list(map(int,input().split()))
  a.append(b)
nittei=[]
for x in range(d):
  nittei.append(int(input()))
  

sum1=sum(a[0][0:26])
ans=[0]*d
humann=a[0]*d
humann=humann+[0]*26



for n in range(d):
  date=nittei[n]
  ans[n]=(a[n+1][date-1])
  try:
    for z in range(26):
      humann[n*26+z]=int(humann[(n-1)*26+z])+int(humann[n*26+z])
  except:
    True
  humann[n*26+date-1]=0
  sum2=sum(humann[n*26+0:n*26+26])
  ans[n]=int(ans[n]) - int(sum2)
  
  
  try:
    ans[n]=ans[n]+ans[n-1]
  except:
    True
    
for y in range(d):
  print(ans[y])


