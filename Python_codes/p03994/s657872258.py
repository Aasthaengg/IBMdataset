
S = input()
s = list(S)

K = int(input())

alp = "abcdefghijklmnopqrstuvwxyz"
dic = {}

for i in range(26):
    dic[alp[i]] = (26 - i) % 26

ind = {}
for i in range(26):
    ind[alp[i]] = i

for i in range(len(s)):


    if K >= dic[s[i]]:
        K -= dic[s[i]]
        s[i] = "a"

    if i == len(s)-1:
        s[i] = alp[ (K + ind[s[i]]) % 26 ]

    #print (s,K)

print ("".join(s))
