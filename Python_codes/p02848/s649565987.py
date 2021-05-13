# ABC146 B - ROT N
N = int(input())
S = str(input())
s=''
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(S)):
    t =alp.index(S[i])+N
    if t>=26:
        t -=26
    s += alp[t]
print(s)