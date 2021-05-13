n = int(input())
p = [[0, 0] for _ in range(n)]
for i in range(n):
  p[i] = list(map(int, input().split()))
p.sort()

st = dict()
for i in range(n-1):
  for j in range(i+1, n):
    st[(p[j][0]-p[i][0], p[j][1]-p[i][1])] = st.get((p[j][0]-p[i][0], p[j][1]-p[i][1]), 0) + 1
  
mx = 0
for key in st:
  mx = max(mx, st[key])
  
print(n-mx)