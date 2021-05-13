n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
all_order={}
def dfs(a):
  if len(a)==n:
    all_order[tuple(a)]=len(all_order.keys())+1
  else:
    for nv in range(n):
      nv+=1
      if nv in a:continue
      dfs(a+[nv])
dfs([])
print(abs(all_order[tuple(p)]-all_order[tuple(q)]))

