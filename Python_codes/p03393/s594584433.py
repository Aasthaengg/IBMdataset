from collections import defaultdict
d = defaultdict(int)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()

if len(S) < 26:
    for x in S:
        d[x] += 1
    for x in a:
        if d[x] == 0:
            print(S+x)
            exit()
else:
    i = 25
    while S[i-1] > S[i]:
        i -= 1
    ss = sorted(list(S[i-1:]))
    t = S[i-1]
    print(S[:i-1] + ss[ss.index(t)+1])
