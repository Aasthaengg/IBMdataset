N,K = map(int,input().split())
h = list(map(int,input().split()))
ans = [0]*N
ans[1] = abs(h[1] - h[0])
for i in range(N - 2):
  j = i + 2
  step = min(K , j)
  height = h[j]
  p = [ans[j - s - 1] + abs(h[j-s-1] - height)
       for s in range(step)]
  ans[j] = min(p)
print(ans[N - 1])  