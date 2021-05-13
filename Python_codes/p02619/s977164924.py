d = int(input())
c = list(map(int, input().split()))
s = []
li = [0]*26

for i in range(d):
    si = list(map(int, input().split()))
    s.append(si)

t = []

for i in range(d):
    t.append(int(input()))

ans = []
day = 0

for i in range(d):
    ti = t[i]
    day += s[i][ti-1]
    li[ti-1] = i+1
    for j in range(26):
        day -= c[j]*(i+1-li[j])
    ans.append(day)

for i in range(d):
    print(ans[i])