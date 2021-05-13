A, V = map(int,input().split())
B, W = map(int,input().split())
T = int(input())
if V<=W:
    print("NO")
else:
    difAB = abs(A-B)
    difVW = V-W
    if difAB<=difVW*T:
        print("YES")
    else:
        print("NO")