n=int(input())
s=list(input())
ans=[]
count=0
num=[]

for i in range(1,n+1):
  l=s[:i]
  r=s[i:]
  
  l=sorted(l)
  r=sorted(r)
  
  for j in l:
    if j in r:
      if j not in num:
        count+=1
        num.append(j)
        
  ans.append(count)
  num.clear()
  count=0
  
print(max(ans))