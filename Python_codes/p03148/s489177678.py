N,K=[int(a) for a in input().split(" ")]
TD = [[int(a) for a in input().split(" ")] for i in range(N)]
TD = sorted(TD, key=lambda arr: arr[1])[::-1]

types = set()
stack = []
ans, totald, i = 0, 0, 0
for i in range(K):
    t, d = TD[i]
    if t in types:
        stack.append(d)
    totald += d
    types.add(t)
ans = totald+len(types)**2

while len(stack)>0:
    while i<N and TD[i][0] in types:
        i+=1
    if i>=N: break
    t1, d1 = TD[i]
    lt = len(types)
    d2 = stack.pop()
    totald -= (d2-d1)
    types.add(t1)
    i+=1
    ans = max(ans, totald+len(types)**2)
print(ans)