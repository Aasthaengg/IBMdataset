A = 'abcdefghijklmnopqrstuvwxyz'
S = input();
if len(S)<26:
    print(S+sorted(set(A)-set(S))[0])
elif S==A[::-1]:
    print(-1); exit()
else:
    _S = S; ans = []
    while len(S)>0:
        ans.append(S[-1]); S = S[:-1]
        ans.sort()
        for a in ans:
            if S[:-1] + a > _S:
                print(S[:-1] + a); exit()