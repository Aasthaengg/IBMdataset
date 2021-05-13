def func(i):
  ret_val=0
  while 0<i:
    ret_val+=i%10
    i//=10
  return ret_val

N=int(input())
ans=10**9
for i in range(1,N):
  j=N-i
  ans=min(ans,func(i)+func(j))
print(ans)
