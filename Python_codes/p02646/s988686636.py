A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

a = V*T+A
b = W*T+B

if V > W:
    if abs(A-B)/(V-W) <= T:
        print("YES")
    else:
        print("NO")
else:
    print("NO")