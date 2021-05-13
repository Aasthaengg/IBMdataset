S = input().strip()
L = len(S)
l = L
while True:
    l -= 1
    for i in range(L-l):
        if len(set(list(S[i:i+l+1]+"ATGC"))) == 4:
            print(len(S[i:i+l+1]))
            exit()
