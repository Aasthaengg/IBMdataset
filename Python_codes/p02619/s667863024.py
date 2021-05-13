n = 26
d = int(input())
c = list(map(int,input().split()))
s = [[] for i in range(d)]
for i in range(d):
    s[i] = list(map(int,input().split()))
a = 0
last = [0]*n
for i in range(d):
    t = int(input())-1
    a += s[i][t]
    last[t] = i+1
    for j in range(n):
        a -= c[j]*(i-last[j]+1)
    print(a)
