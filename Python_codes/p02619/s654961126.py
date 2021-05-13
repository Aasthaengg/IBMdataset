D = int(input())
c = list(map(int,input().split()))
s = []
for i in range(D):
    s.append(list(map(int,input().split())))
t = []
for i in range(D):
    t.append(int(input()))

def last(d,la):
    s = 0
    for i in range(26):
        s += c[i] * (d - la[i])
    return s

lastday = [0]*26
a = 0
for d in range(D):
    lastday[t[d]-1] = d + 1
    a += s[d][t[d]-1]- last(d+1,lastday)
    print(a)