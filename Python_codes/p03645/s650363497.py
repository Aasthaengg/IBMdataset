n,m = map(int,input().split())
a_lst = []
for i in range(m):
  a_lst.append( list(map(int,input().split())) )
 
ans = "IMPOSSIBLE"
 
start_lst = []
goal_lst = []
for a in a_lst:
  if a[0] == 1:
    start_lst.append(a[1])
  if a[1] == n:
    goal_lst.append(a[0])
goal_lst = set(goal_lst)
for s in start_lst:
  if s in goal_lst:
    ans = "POSSIBLE"
    
print(ans)