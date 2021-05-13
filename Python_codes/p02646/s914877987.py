A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

# 鬼よりBが左
if A > B:
    if A - V*T <= B - W*T:
        print("YES")
    else:
        print("NO")
else:
    if A + V*T >= B + W*T:
        print("YES")
    else:
        print("NO")