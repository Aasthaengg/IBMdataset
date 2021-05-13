a=input()
dic={}
for i in range(len(a)):
  s=a[i]
  if s in dic:
    dic[s]=dic[s]+1
  else:
    dic[s]=1

sum=0
for val in dic.values():
  if val>1:
    sum=sum+(val-1)*val//2
  
print((len(a)*(len(a)-1))//2-sum+1)