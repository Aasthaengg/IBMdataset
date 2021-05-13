S=input()
abc=[chr(ord('a')+i) for i in range(26)]

if len(S)<26:
    for s in S:
        abc.remove(s)
    print(S+abc[0])
    exit()
for i in range(24,-1,-1):
    for j in range(25,i,-1):
        if S[i]<S[j]:
            print(S[:i]+S[j])
            exit()

print(-1)
