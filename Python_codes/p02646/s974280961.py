A, V = map(int, input().split())                                               
B, W = map(int, input().split())                                               
T = int(input())

if A < B:
    A_res = A + V * T
    B_res = B + W * T

    if A_res >= B_res:
        print("YES")
    else:
        print("NO")

else:
    A_res = A - V * T
    B_res = B - W * T

    if A_res <= B_res:
        print("YES")
    else:
        print("NO")