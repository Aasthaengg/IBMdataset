A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    print("NO")
    exit()

d = abs(A - B)
s = V - W

if d <= s * T:
    print("YES")
else:
    print("NO")
