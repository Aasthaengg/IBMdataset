A, B, C, K = list(map(int, input().split()))

if K%2 == 0:
  if A-B > 10**18:
    print("Unfair")
  else:
    print(A-B)
else:
  if -(A-B) > 10**18:
    print("Unfair")
  else:
    print (-(A-B))