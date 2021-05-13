alp=[chr(ord('a') + i) for i in range(26)]
unused=set(alp)
     
S=input()
#print("len",len(S))

if len(S)<26:
    for i in range(len(S)):
        if S[i] in unused:
            unused.remove(S[i])
    unused=sorted(unused)
    print(S+unused[0])
else:
    for j in range(len(S)-1,-1,-1):
        p=set(S[j:])
        #print(p)
        q=sorted(p)
        if S[j]==q[-1]:
            pass
        else:
            idx=q.index(S[j])
            print(S[:j]+q[idx+1])
            break
    else:
        print(-1)