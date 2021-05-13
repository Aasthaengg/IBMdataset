S = list(input())
N = len(S)
al = [chr(ord('a') + i) for i in range(26)]
if N!=26:
    D = dict(zip(al,[0]*26))
    cand = []
    for i in range(N):
        D[S[i]]+=1
    for key in D.keys():
        if D[key]==0:
            cand.append(key)
    cand.sort()
    S.append(cand[0])
    print("".join(S))
else:
    if S==list(reversed(al)):
        print(-1)
    else:
        cand = []
        for i in range(26):
            if S[25-i-1]>S[25-i]:
                cand.append(S[25-i])
                continue
            else:
                change_ind = 25-i
                cand.append(S[25-i])
                break
        cand.sort()
        T = S[0:change_ind]
        i = 0
        while True:
            if T[-1]<cand[i]:
                T[-1]=cand[i]
                break
            i+=1
        print("".join(T))