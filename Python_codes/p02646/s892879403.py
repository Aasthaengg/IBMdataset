A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    ans = "NO"
else:
    if abs(A - B) / (V - W) <= T:
        ans = "YES"
    else:
        ans = "NO"
print(ans)
