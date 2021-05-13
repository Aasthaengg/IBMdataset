N,M = map(int,input().split())
Alist = list(map(int, input().strip().split()))
r = [0]*N
r[0] = Alist[0]
for i in range(1,len(Alist)):
    r[i] = r[i-1] + Alist[i]
for i in range(len(r)):
    r[i] = r[i]%M
r.sort()
p = []
m = 0
for i in range(len(r)-1):
    m = m+1
    if r[i] != r[i+1]:
        p.append(m)
        m = 0
    if i == len(r)-2:
        p.append(m+1)
x = 0
for i  in range(len(r)):
    if r[i] == 0:
        x = x +1
def combi(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    else:
        return (n*(n-1))/2
s = 0
for i in range(len(p)):
    s = s + combi(p[i])
s = s + x
print(int(s))