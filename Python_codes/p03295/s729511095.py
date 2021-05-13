n,m = map(int,input().split())

li2=[input() for i in range(m)]
ab = []
for i in range(m):
    ab.append( [int(x.strip()) for x in li2[i].split()])

ab = sorted(ab,key=lambda x:x[1])

ans_last = ab[0][1]
ans = 1

for i in range(1,m):
    a = ab[i][0]
    b = ab[i][1]
    if b > ans_last and a >= ans_last:
        ans_last = b
        ans += 1

print(ans)