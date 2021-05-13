N = int(input())
S = list(input())
cnt_E = [S.count("E")]
flag = True
if S[0] == "W":
    cnt_W = [1]
else:
    cnt_W = [0]
    flag = False
SUM = [cnt_E[0]+cnt_W[0]]
for i in range(1,N):
    if S[i] == "W":
        cnt_W.append(cnt_W[i-1]+1)
        cnt_E.append(cnt_E[i-1])
    else:
        cnt_W.append(cnt_W[i-1])
        if flag:
            cnt_E.append(cnt_E[i-1])
            flag = False
        else:
            cnt_E.append(cnt_E[i-1]-1)
    SUM.append(cnt_W[i]+cnt_E[i])
print(min(SUM)-1)