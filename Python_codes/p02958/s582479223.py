import sys
N = int(input())
P = list(map(int,input().split()))

ans = sorted(P)

if P == ans:
  print("YES")
else:
  for i in range(N-1):
    for j in range(i+1,N):
      check = []
      check += P
      check[i],check[j] = check[j],check[i]
      if check == ans:
        print("YES")
        sys.exit()
  print("NO")