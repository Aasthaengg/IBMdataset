N = int(input())
M = set()
MM = input().split()
for i in MM:
  M.add(i)

if len(M) == 3:
  print('Three')
else:
  print('Four')