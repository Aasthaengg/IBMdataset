S = input()
if len(S) == 26:
    last = None
    l = [False for i in range(26)]
    for i, s in enumerate(S):
        l[ord(s)-ord('a')] = True
        o = ord(s)-ord('a')
        while o <= ord('z')-ord('a'):
            if l[o] == False:
                last = S[:i] + chr(ord('a') + o)
                break
            o += 1
    if last:
        print(last)
    else:
        print(-1)
else:
    l = [False for i in range(26)]
    for s in S:
        l[ord(s)-ord('a')] = True
    for i in range(26):
        if l[i] == False:
            print(S+chr(ord('a') + i))
            break
