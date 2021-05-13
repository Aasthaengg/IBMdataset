deg = [0] * 5
for _ in range(3):
  a,b = map(int,input().split())
  deg[a] += 1
  deg[b] += 1

bl = max(deg) <= 2
answer = 'YES' if bl else 'NO'
print(answer)