N,A,B = map(int,input().split())
smax = min(A,B)
smin = max(A+B-N,0)
print(smax,smin)