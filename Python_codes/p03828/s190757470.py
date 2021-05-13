n=int(input())
p_list=[]
m=1
for i in range(1,n+1):
  m*=i
  if i==1:
    pass
  elif i==2:
    p_list.append(2)
  else:
    div=0
    for j in p_list:
      if i%j==0:
        div+=1
        break
    if div==0:
      p_list.append(i)

ans=1
for i in p_list:
  s=0
  aaa=0
  while aaa==0:
    if m%i==0:
      s+=1
      m=m//i
    else:
      aaa+=1
  s+=1
  ans*=s

print(ans%(10**9+7))