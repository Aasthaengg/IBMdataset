ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k = ni()

p = [[0]*10 for _ in range(10)]

for i in range(k+1):
  s = [int(_) for _ in str(i)]
  p[s[0]][s[-1]]+=1

ans=0

for i in range(1,10):
  for j in range(1,10):
    ans += p[i][j] * p[j][i]

print(ans)