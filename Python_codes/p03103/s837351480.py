n,m = map(int,input().split())
a_b = {}
for i in range(n):
    x,y = map(int,input().split())
    if x in a_b.keys():
        a_b[x] += y
        continue
    a_b[x] = y
a_b = sorted(a_b.items(), key=lambda x:x[0])

#print(a_b)
c = 0
ans = 0
t = 0
for i in range(int(len(a_b))):
    c += a_b[i][1]
    if c > m:
        ans += a_b[i][0] * (m - t)
        break
    else:
        ans += a_b[i][0] * a_b[i][1]
        t += a_b[i][1]

print(ans)
