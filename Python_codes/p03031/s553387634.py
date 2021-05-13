n,m = map(int,input().split())

switch = []

for i in range(m):
    switch.append(list(map(lambda x:int(x)-1 ,input().split()))[1:])
p = list(map(int,input().split()))


ans = 0
for i in range(2**n):
    s = []
    for j in range(n):
        s.append((i>>j)&1)
    f = 1
    for j in range(m):
        a = 0
        for k in switch[j]:
            a += s[k]

        if a%2== p[j]:
            pass
        else:
            f = 0
            break

    if f:
        ans += 1

print(ans)