import math
S = input()
L = len(S)
Rcount = 0
Lcount = 0
r = 0
l = 0
i = 0
ans = [0] * L
while i < L:
    #Rの数
    while True:
        if S[i] == "R":
            i+=1
            Rcount += 1
        else:
            break
    r = i-1
    #Lの数
    while i<L:
        if S[i] == "L":
            i+=1
            Lcount += 1
        else:
            break
    l = r+1
    ans[l] = math.floor(Rcount/2) + math.ceil(Lcount/2)
    ans[r] = math.floor(Lcount/2) + math.ceil(Rcount/2)
    Rcount = 0
    Lcount = 0
print(*ans)