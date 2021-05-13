while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    a = [["#" for j in range(W)] for i in range(H)]
    b = ["".join(a[i]) for i in range(H)]
    print(b[0])
    coma = ["."for i in range(W-2)]
    coma = "".join(coma)
    for i in range(H-2):
        print("#"+coma+"#")
    print(b[H-1])
    print()