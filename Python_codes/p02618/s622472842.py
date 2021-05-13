d = int(input())
c = list(map(int,input().split()))
s = []
p = [1]*d
for i in range(d):
    s.append(list(map(int,input().split())))
x = [1]*26
for i in range(d):
    q = 1
    m = -1
    for j in range(26):
        n = s[i][j] + (x[j]+13)*(x[j]+14)*c[j]
        x[j] += 1
        if(m < n):
            m = n
            q = j
    x[q] *= 0
    p[i] = q+1
for i in range(d):
    print(p[i])