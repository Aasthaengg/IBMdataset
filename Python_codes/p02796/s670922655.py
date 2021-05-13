N = int(input())
X = [];L =[]
for i in range(N):
  x,l = map(int,input().split())
  X.append(x);L.append(l)
#print(X,L)
Y = []
for i in range(N):
  a = X[i]-L[i];b=X[i]+L[i]
  Y.append([a,b])
#print(Y)
Y.sort(key=lambda x : x[1])
ans = 0
end = - float("inf")
for i in range(N):
  if end > Y[i][0]:
    continue
  ans += 1
  end = Y[i][1]
print(ans)
