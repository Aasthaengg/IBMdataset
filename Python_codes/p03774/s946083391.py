n, m = map(int, input().split())
stud = []
poit = []
for i in range(n):
    a, b = map(int, input().split())
    stud.append([a, b])
for i in range(m):
    c, d = map(int, input().split())
    poit.append([c, d])
    
for a, b in stud:
    dist = float('inf')
    for i, info in enumerate(poit):
        c = info[0]
        d = info[1]
        mdist = abs(a-c) + abs(b-d)
        if dist > mdist:
            dist = mdist
            ans = i+1
    print(ans)
    # print(i, info)
