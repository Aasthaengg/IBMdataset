import bisect
n=int(input())
X=list(map(int,input().split()))
sortX = sorted(X)
ansl = sortX[n//2-1]
ansu = sortX[n//2]
for x in X:
  if bisect.bisect(sortX,x) > n//2:
    print(ansl)
  else:
    print(ansu)