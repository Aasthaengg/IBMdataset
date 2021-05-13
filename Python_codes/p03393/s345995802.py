S = input()
se = set()
for s in S:
    se.add(s)
if len(S) < 26:
    for i in range(26):
        s = chr(ord('a')+i)
        if not s in se:
            print(S+s)
            exit()
else:
    while len(S) > 1:
        se.remove(S[-1])
        S = S[:-1]
        for i in range(ord(S[-1]), ord('z')+1):
            s = chr(i)
            if not s in se:
                print(S[:-1]+s)
                exit()
print(-1)
