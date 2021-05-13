s = input()
K = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
for alp in alphabet:
    if alp not in s:
        continue
    sub = set()
    for i,S in enumerate(s):
        if S == alp:
            for j in range(i,min(i+5,len(s))):
                sub.add(s[i:j+1])
    if len(sub) < K:
        K -= len(sub)
    else:
        l_sub = list(sub)
        l_sub.sort()
        print(l_sub[K-1])
        exit()
