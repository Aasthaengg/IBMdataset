D = int(input())
s = [input() for i in range(2*D+1)]
for i in range(0,2*D+1):
    s[i] = s[i].split()
    s[i] = [int(p) for p in s[i]]
a = []
b = [0]*len(s[0])
S = 0
m = 0
for i in range (1,D+1):
    for j in range(0,len(s[0])):
        if j == s[D+i][0]-1:
            b[s[D+i][0]-1] = 0
        else:
            b[j] = b[j] + s[0][j]
    S = S + s[i][s[D+i][0]-1] - sum(b)
    a.append(S)
for i in (a):
    print(i)