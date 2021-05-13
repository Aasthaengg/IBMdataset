N, Q = map(int, input().split())
S = input()
l = []
r = []
for q in range(Q):
    a,b = map(int, input().split())
    l.append(a)
    r.append(b)

s = [0, 0]
for j in range(1, N):
    if S[j-1]=='A' and S[j]=='C':
        s.append(s[-1]+1)
    else:
        s.append(s[-1])

for q in range(Q):
    print(s[r[q]] - s[l[q]])