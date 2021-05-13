import collections
S = input()

if(S == "zyxwvutsrqponmlkjihgfedcba"):
    print(-1)
    exit()
    
alp = "abcdefghijklmnopqrstuvwxyz"
r = S[::-1]

c = collections.Counter(S)
c_s = sorted(c.items(), key=lambda x:x[0])
tmp = ""

for i in range(len(c_s)):
    tmp += c_s[i][0]

if(len(S) < 26):
    for i in range(len(alp)):
        if(alp[i] not in tmp):
            print(S+alp[i])
            break
else:
    for i in range(len(S)-1):
        if(r[i] > r[i+1]):
            cha = sorted(r[:(i+1)])
            for j in range(len(cha)):
                if(cha[j] > r[i+1]):
                    print(S[:(len(S)-i-2)]+cha[j])
                    exit()