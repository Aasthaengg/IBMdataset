N, M, X, Y = map(int, input().split())
p = max(map(int, input().split()))
q = min(map(int, input().split()))
for Z in range(X+1, Y+1):
  if p<Z and Z<=q:
    print("No War")
    break
else:
  print("War")