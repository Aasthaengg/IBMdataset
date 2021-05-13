n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_=[0]
for i in range(len(a)):
  a_.append(a_[-1]+a[i])
b_=[0]
for i in range(len(b)):
  b_.append(b_[-1]+b[i])
ans=[0]
a_now=0
b_now=m
for i in range(n+1):
  k_=k-a_[i]
  while b_[b_now]>k_:
    b_now+=-1
    if b_now==-1:
      b_now=0
      break
  if a_[i]+b_[b_now]<=k:
    ans.append(i+b_now)
print(max(ans)) 
