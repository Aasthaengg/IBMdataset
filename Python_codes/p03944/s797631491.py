W, H, N = list(map(int, input().split()))

X = [0] * N
Y = [0] * N
A = [0] * N

for _ in range(N):
    X[_], Y[_], A[_] = list(map(int, input().split()))

# print("test")
# print(W,H,N)

#solve
xb = 0
xe = W
yb = 0
ye = H

for _ in range(N):
    if A[_] == 1:
        # Xiより小さいを黒
        xb = max([xb, X[_]])
    elif A[_] == 2:
        # Xiより大きいを黒
        xe = min([xe, X[_]])
    elif A[_] == 3:
        # Yiより小さいを黒
        yb = max([yb, Y[_]])
    else:
        # Yiより大きいを黒
        ye = min([ye, Y[_]])
    
    # check
    if (xe - xb) <= 0 or (ye - yb) <= 0:
        print(0)
        import sys
        sys.exit()

ans = (xe - xb) * (ye - yb)
print(ans)