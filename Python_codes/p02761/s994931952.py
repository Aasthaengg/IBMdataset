N,M = map(int,input().split())
C = [input().split() for m in range(M)]

for n in range(1000):
  n = str(n)
  if len(n)==N:
    for s,c in C:
      if n[int(s)-1]!=c:
        break
    else:
      print(n)
      exit()

print(-1)