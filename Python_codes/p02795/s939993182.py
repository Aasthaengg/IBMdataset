H = int(input())
W = int(input())
N = int(input())
A = max(H, W)
ans = (N + A - 1) // A
print(ans)
