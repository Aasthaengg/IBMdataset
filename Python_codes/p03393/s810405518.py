S = input()
if len(S)<26:
    for c in map(chr, range(97,123)):
        if c not in S:
            print(S+c)
            exit()
for i in range(26):
    for c in map(chr, range(ord(S[25-i])+1,ord('z')+1)):
            if c not in S[0:25-i]:
                print(S[0:25-i]+c)
                exit()
print(-1)
