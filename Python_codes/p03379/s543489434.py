N=int(input())
X=list(map(int, input().split()))
Y=sorted(X)
mae=Y[N//2-1]
ato=Y[N//2]

for x in X:
  if x<=mae:
    print(ato)
  elif x>=ato:
    print(mae)