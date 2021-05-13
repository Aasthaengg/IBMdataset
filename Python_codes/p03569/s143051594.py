S = list(input())
N = len(S)

cnt = 0
l = 0
r = N-1
while l<=r:
    if S[l]=="x" and S[r]!="x":
        l += 1
        cnt += 1
    elif S[l]!="x" and S[r]=="x":
        r += -1
        cnt += 1
    elif S[l]=="x" and S[r]=="x":
        l += 1
        r += -1
    elif S[l]!="x" and S[r]!="x":
        if S[l]==S[r]:
            l += 1
            r += -1
        else:
            cnt = -1
            break
print(cnt)