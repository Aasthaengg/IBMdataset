def II(): return int(input())
N=II()
def solve(n):
  tbl=[0]*100
  ans=0
  for i in range(1,n+1):
    i=str(i)
    tbl[int(i[0]+i[-1])]+=1
  for i in range(1,n+1):
    i=str(i)
    ans+=tbl[int(i[-1]+i[0])]
  return ans
a=solve(N)
print(a)      