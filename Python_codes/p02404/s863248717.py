def print_side(W):
    for j in range(W):
        print("#",end="")
    print("")

def print_body(W):
    for j in range(W):
        if j==0 or j==W-1: 
            print("#",end="")
        else:
            print(".",end="")
    print("")

while True:
    H,W = [int(x) for x in input().split()]
    if (H,W)==(0,0): break
    for i in range(H):
        if i==0 or i==H-1:
            print_side(W)
        else:
            print_body(W)
    print("")