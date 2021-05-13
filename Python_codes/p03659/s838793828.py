n=int(input())
a=list(map(int,input().split()))
s_lst=[0]
for i,aa in enumerate(a):
  s_lst.append(s_lst[i]+aa) # len(s_lst): n+1
s_all=s_lst[-1]
ans=float("inf")
for i in range(1,len(s_lst)-1):
  ans=min(ans,abs(2*s_lst[i]-s_all))
print(ans)
