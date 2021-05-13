N ,Q = map(int,input().split())
S = input()
lst = []
for i in range(Q):
    s,e = map(int,input().split())
    lst.append([s-1,e-1])
#print(lst)

cum = [0]*N
for i in range(1,N):
    if S[i-1] == 'A' and S[i] == 'C':
        cum[i] = cum[i-1] + 1
    else:
        cum[i] = cum[i - 1]

for v in lst:
    print(cum[v[1]] - cum[v[0]])