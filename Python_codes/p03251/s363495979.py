n,m,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x = sorted(x)
y = sorted(y)
ok = False
for i in range(X+1,Y+1):
    if x[n-1] < i and y[0] >= i:
        ok = True
        break
if ok == 1: print("No War")
else: print("War")