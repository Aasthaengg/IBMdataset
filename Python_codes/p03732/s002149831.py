N,W = map(int,input().split())

w0,v0 = map(int,input().split())
vlist = [[v0],[],[],[]]

for i in range(N-1):
    w,v = map(int,input().split())
    vlist[w-w0].append(v)

for i in range(4):
    vlist[i].sort(reverse = True)

m = 0
S = [[0],[0],[0],[0]]
for i in range(4):
    for j in range(len(vlist[i])):
        S[i].append(S[i][-1]+vlist[i][j])

m = 0
for i in range(len(S[0])):
    for j in range(len(S[1])):
        for k in range(len(S[2])):
            for l in range(len(S[3])):
                if w0*(i+j+k+l)+j+2*k+3*l <= W:
                    m = max(m,S[0][i]+S[1][j]+S[2][k]+S[3][l])

#print(vlist)
#print(S)
print(m)