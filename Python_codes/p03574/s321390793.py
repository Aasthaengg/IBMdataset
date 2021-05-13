H,W = map(int,input().split())
S = ["."*(W+2)]
for i in range(H):
    x=input().strip()
    x = "."+x+"."
    S.append(x)
S.append("."*(W+2))
A = [[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j]=="#":
            A[i][j] = "#"
        else:
            cnt = 0
            if S[i][j+1]=="#":
                cnt += 1
            if S[i-1][j+1]=="#":
                cnt += 1
            if S[i-1][j]=="#":
                cnt += 1
            if S[i-1][j-1]=="#":
                cnt += 1
            if S[i][j-1]=="#":
                cnt += 1
            if S[i+1][j-1]=="#":
                cnt += 1
            if S[i+1][j]=="#":
                cnt += 1
            if S[i+1][j+1]=="#":
                cnt += 1
            A[i][j]=str(cnt)
    print("".join(A[i][1:W+1]))