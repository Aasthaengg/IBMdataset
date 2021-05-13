n=int(input())
l=list(map(int,input().split()))

if n==2:
  print(sum(l)*2)
else:
  ans=[]
  ans.append(l[0])
  ans.append(l[len(l)-1])

  for i in range(len(l)-1): 
    num=min(l[i],l[i+1])
    ans.append(num)
  
  print(sum(ans))