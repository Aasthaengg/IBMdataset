H, W, A, B = map(int, input().split())

for h in range(B):
    print("1"*A+"0"*(W-A))
for h in range(H-B):
    print("0"*A+"1"*(W-A))