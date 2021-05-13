N, T = map(int, input().split())
result = []
for i in range(N):
  c, t = map(int, input().split())
  if T >= t:
    result.append([c,t])
print((sorted(result, key=lambda x:x[0])[0][0]) if result else 'TLE')