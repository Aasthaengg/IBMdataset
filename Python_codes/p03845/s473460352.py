n = int(input())
t = list(map(int, input().split()))
m = int(input())
p_x = []
for _ in range(m):
  p, x = map(int, input().split())
  p_x.append([p, x])
for i in p_x:
  p = i[0]
  x = i[1] 
  ans = sum(t) - t[p-1] + x
  print(ans)