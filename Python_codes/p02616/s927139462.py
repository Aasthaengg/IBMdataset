MOD = 10 ** 9 + 7
 
N, K = map(int, input().split())
l = list(map(int, input().split()))
pos = []
neg = []
z = 0
 
for v in l:
    if v > 0:
        pos.append(v)
    elif v < 0:
        neg.append(v)
    else:
        z += 1
pos.sort()
neg.sort()
 
if N - z < K:
    print(0)
elif N - z == K:
    if len(neg) % 2 and z:
        print(0)
    else:
        out = 1
        for v in neg + pos:
            out *= v
            out %= 10 ** 9 + 7
        print(out)
elif len(pos) == 0:
    if K % 2:
        if z:
            print(0)
        else:
            neg.reverse()
            out = 1
            for i in range(K):
                out *= neg[i]
                out %= 10 ** 9 + 7
            print(out)
    else:
        out = 1
        for i in range(K):
            out *= neg[i]
            out %= 10 ** 9 + 7
        print(out)
else:
    out = 1
    neg.reverse()
    if K % 2:
        out = pos.pop()
        K -= 1
    while K:
        if len(pos) >= 2:
            nP = pos[-1] * pos[-2]
        else:
            nP = 0
 
        if len(neg) >= 2:
            nN = neg[-1] * neg[-2]
        else:
            nN = 0
 
        if nP > nN:
            pos.pop()
            pos.pop()
            out *= nP
        else:
            neg.pop()
            neg.pop()
            out *= nN
        out %= MOD
        K -= 2
    print(out)
