def print_line(W,even_char,odd_char):
    for j in range(W):
        if j%2==0:
            print(even_char,end="")
        else:
            print(odd_char,end="")
    print("")

while True:
    H,W = [int(x) for x in input().split()]
    if (H,W)==(0,0): break
    for i in range(H):
        if i%2==0:
            print_line(W,"#",".")
        else:
            print_line(W,".","#")
    print("")