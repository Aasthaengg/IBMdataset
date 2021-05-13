a = list(map(int, input().split()))

b = [a[0]-a[2], a[1]-a[3]]
c = [b[1]+a[2], -b[0]+a[3]]

d = [a[2]-c[0], a[3]-c[1]]
e = [d[1]+c[0], -d[0]+c[1]]

ans = []
ans.append(c[0])
ans.append(c[1])
ans.append(e[0])
ans.append(e[1])

L = [str(a) for a in ans]
L = ' '.join(L)
print(L)