A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if(V-W > 0):
    if(abs(A-B)/(V-W) <= T):
        print("YES")
    else:
        print("NO")
else:
    print("NO")