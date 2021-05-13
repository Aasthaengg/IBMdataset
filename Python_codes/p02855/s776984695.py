h,w,k = map(int,input().split())
S = []
for i in range(h):
    S.append(list(input()))
cnt = 0
flag = False
for i in range(h):
    for j in range(w):
        if flag:
            if S[i][j] == "#":
                cnt += 1
            S[i][j] = str(cnt)
        else:
            if S[i][j] == "#":
                cnt += 1
                flag = True
                S[i][j] = str(cnt)
                if j != 0:
                    for k in range(j):
                        S[i][k] = str(cnt)
    flag = False
for i in range(h):
    k = i
    for j in range(w):
        if S[i][j] == ".":
            while S[k][j] == ".":
                k += 1
                if k > h-1:
                    break
            if k <= h-1:
                S[i] = S[k]
            else:
                l = i
                while S[l][j] == ".":
                    l -= 1
                S[i] = S[l]
for i in range(h):
    print(" ".join(S[i]))            