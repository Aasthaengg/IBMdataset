S = input()

max_cnt = 0
for i in range(len(S)):
    cnt = 0
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        cnt += 1
        for j in range(len(S)-(1+i)):
            if S[j+i+1] == "A" or S[j+i+1] == "C" or S[j+i+1] == "G" or S[j+i+1] == "T":
                cnt += 1
            else:
                break
    if cnt >= max_cnt:
        max_cnt = cnt
print(max_cnt)