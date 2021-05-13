d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
t = [int(input()) for i in range(d)]
mem = [0 for i in range(26)]
v = 0
su = sum(c)
for a in range(d):
    v += s[a][t[a]-1]
    mem[t[a]-1] = a+1
    for i in range(26):
        v -= c[i]*(a+1 - mem[i])
    print(v)