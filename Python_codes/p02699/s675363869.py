S, W = list(map(int, input().split()))

ans = "unsafe"
if S > W:
    ans = "safe"

print(ans)