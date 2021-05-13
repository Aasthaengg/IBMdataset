n,m,x,y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
z1 = max(A)+1
z2 = min(B)
for i in range(x+1,y+1):
    if z1 <= i <= z2:
        print("No War")
        break
else:
    print("War")