H = int(input())
W = int(input())
N = int(input())

print(N//max(H,W) if N%max(H,W) == 0 else N//max(H,W)+1)