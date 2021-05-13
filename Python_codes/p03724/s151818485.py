import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ln = [0]*n
for i in range(m):
  a,b = map(int,input().split())
  ln[a-1] += 1
  ln[b-1] += 1
  
for i in ln:
  if i%2:
    print('NO')
    exit()
print('YES')