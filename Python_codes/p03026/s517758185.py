n = int(input())
tree = [set() for i in range(n)]
con = [0]*n
ans = [0]*n
scr = 0
for _ in range(n-1):
  a,b = map(lambda x:int(x)-1, input().split())
  tree[a].add(b)
  tree[b].add(a)
  con[a] += 1
  con[b] += 1
st = []
for i in range(n):
  if con[i] == 1:
    st.append(i)
c = list(map(int, input().split()))
c.sort(reverse=True)
while st:
  v = st.pop()
  if ans[v]:
    continue
  ans[v] = c.pop()
  scr += ans[v]*con[v]
  con[v] = 0
  for x in tree[v]:
    if ans[x]:
      continue
    con[x] -= 1
    if con[x] <= 1:
      st.append(x)
print(scr)
print(" ".join(map(str,ans)))