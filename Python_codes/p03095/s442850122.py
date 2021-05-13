n=int(input())
s=input()
m=10**9+7
dict={}
for i in s:
  if i not in dict:
    dict[i]=1
  else:
    dict[i]+=1
ans=1
for i in dict:
  ans*=dict[i]+1
print((ans-1)%m)