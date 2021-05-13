[W, H, x, y] = [int(i) for i in input().split()]
ans = 0
if x * 2 == W and y * 2 == H:
    ans = 1
print(str(W*H/2.0)+' '+str(ans))
