n,x = map(int,input().split())
mina = 10**9
cnt = 0
for i in range(n):
  a = int(input())
  x -= a
  cnt += 1
  mina = min(a,mina)
  
cnt += x//mina
print(cnt)