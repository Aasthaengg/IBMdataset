n,m = map(int,input().split())
a_b = [list(map(int,input().split())) for _ in range(m)]
a_b = sorted(a_b,key=lambda x:x[0])

s = set()
for i in range(m):
    if a_b[i][0] == 1:
        s.add(a_b[i][1])
for i in range(m):
    if a_b[i][0] in s:
        if a_b[i][1] == n:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')
