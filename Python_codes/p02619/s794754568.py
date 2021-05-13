D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(D)]
t = [int(input()) for i in range(D)]

last = {}
for i in range(1,27):
    last[i] = 0

satisfaction = 0
for d in range(1,D+1):
    satisfaction += s[d-1][t[d-1]-1]
    last[t[d-1]] = d
    for i in range(1,27):
        satisfaction -= c[i-1]*(d-last[i])
    print(satisfaction)
