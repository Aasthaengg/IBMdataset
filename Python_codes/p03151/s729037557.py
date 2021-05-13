n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = [0]*n
e = 0
t = 0
for i in range(n):
    d[i] = a[i] - b[i]
    if d[i] < 0:
        e += 1
        t -= d[i]
d = sorted(d,reverse=True)
if sum(d) < 0:
    ans = -1
else:
    s = 0
    for i in range(n):
        if s >= t:
            break
        else:
            s += d[i]
    ans = i + e
print(ans)