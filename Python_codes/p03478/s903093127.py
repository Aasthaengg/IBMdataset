N,A,B = map(int, input().split())


X = [0]*10100
for i in range(len(X)):
  S = str(i)
  a = 0
  for c in S:
    a += int(c)

  X[i] = a

# print( X )

ans = 0
for i,x in enumerate(X[:N+1]):
  if A<=x and x<=B:
    ans += i
    # print(i, ans)

print(ans)
