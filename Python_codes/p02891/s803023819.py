import math
S = input()
K = int(input())
s = list(S)
c1 = 0
for i in range(len(s)-1):
    if s[i+1] == s[i]:
        c1 += 1
        s[i+1] = 0
s = list(S*2)
c2 = 0
for i in range(len(s)-1):
    if s[i+1] == s[i]:
        c2 += 1
        s[i+1] = 0
c = S[0]
for s in S:
    if s != c:
        print(c1+(c2-c1)*(K-1))
        exit()
print(math.floor(len(S)*K/2))
