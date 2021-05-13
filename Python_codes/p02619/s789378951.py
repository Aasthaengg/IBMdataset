D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]
v = 0
last = [0 for _ in range(len(c))]

for day in range(D):
    v += s[day][t[day]-1] 
    last[t[day]-1] = day + 1
    for j in range(len(c)):
        v -= c[j]*(day + 1 - last[j])
    print(v)