def dec(day):
    ret = 0
    for i in range(26):
        ret += c[i]*(day-last[i])
    return ret


d = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for _ in range(d)]
last = [0]*26

ans = 0
for i in range(d):
    t = int(input())
    ans += s[i][t-1]
    last[t-1] = i+1
    ans -= dec(i+1)
    print(ans)