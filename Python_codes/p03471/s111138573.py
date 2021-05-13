N,Y = map(int,input().split())

ans = [-1,-1,-1]

for n1 in range(N+1):
  for n2 in range(N-n1+1):
    yen = n1 * 10000 + n2 * 5000 + (N-n1-n2) * 1000
    if yen == Y:
      ans = [n1,n2,N-n1-n2]
      break

print(" ".join(map(str,ans)))