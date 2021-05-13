import sys
A, B = map(int, input().split())
 
for i in range(10 ** 5):
  if int(i * 0.08) == A and int(i * 0.1) == B:
    print(i)
    sys.exit()
  else:
    continue
else:
  print(-1)