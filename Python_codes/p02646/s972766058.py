A_V = input().split(" ")
B_W = input().split(" ")
T = int(input())
A = int(A_V[0])
V = int(A_V[1])
B = int(B_W[0])
W = int(B_W[1])
dA = A + V * T
dB = B + W * T
ndA = A - V * T
ndB = B - W * T
if (A<B):
    if (dA < dB):
        print("NO")
    else:
        print("YES")
else:
    if (ndA > ndB):
        print("NO")
    else:
        print("YES")