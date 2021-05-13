N,M,X,Y = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Xmax = max(A)
Ymin = min(B)
out = "War"
Xmax = max(Xmax,X)
Ymin = min(Ymin,Y)
if Xmax<Ymin:
    out = "No War"
print(out)
