import bisect

def last(d,i):
    x = bisect.bisect_right(last_hol[i],d,)
    #print(x,last_hol[i])
    if x == 0:
        return 0
    else:
        return last_hol[i][x-1]

d = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(d)]
last_hol = {i:[] for i in range(1,27)}
t = []
for i in range(d):
    ti = int(input())
    last_hol[ti].append(i+1)
    t.append(ti)
ans = 0
a = [0]*d
for i in range(d):
    ti = t[i]
    ans += s[i][ti-1]
    for j in range(1,27):
        ans -= c[j-1]*(i+1-last(i+1,j))
    print(ans)