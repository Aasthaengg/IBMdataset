H = int(input())
W = int(input())
N = int(input())
v = max(H, W)
ans = N // v
if N%v != 0:
    ans += 1

print(ans)