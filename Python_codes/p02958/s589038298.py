n = int(input())
s = list(map(int, input().split()))

S = sorted(s)

count=0
for i in range(n):
  if s[i] != S[i]:
    count += 1
    
if count == 0 or count == 2:
  print('YES')
else:
  print('NO')