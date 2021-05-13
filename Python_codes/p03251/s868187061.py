n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ans = [i for i in range(X+1,Y+1)]
for i in ans:
  if max(x) < i:
    if min(y) >= i:
      print('No War')
      exit()
print('War')