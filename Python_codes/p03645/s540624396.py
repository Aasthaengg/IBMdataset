n,m = map(int,input().split())

start_set = set()
goal_set = set()
for i in range(m):
  s,g = map(int,input().split())
  if s == 1:
    start_set.add(g)
  if g == n:
    goal_set.add(s)    

ans = "POSSIBLE" if (start_set & goal_set) else "IMPOSSIBLE"
print(ans)