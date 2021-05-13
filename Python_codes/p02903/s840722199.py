def LI():
    return list(map(int, input().split()))


H, W, A, B = LI()
S = "1"*A+"0"*(W-A)
for _ in range(B):
    print(S)
S = "0"*A+"1"*(W-A)
for _ in range(H-B):
    print(S)
