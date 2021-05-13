S=input()
if len(S)<26:
    print(S+sorted(list({chr(i+97) for i in range(26)}-set(S)))[0])
else:
    tmp = [S[25]]
    for i in range(25):
        tmp.append(S[24-i])
        if S[24-i] < S[25-i]:
            tmp =sorted(tmp)
            print(S[:26-len(tmp)]+tmp[tmp.index(S[24-i])+1])
            exit()
    print(-1)