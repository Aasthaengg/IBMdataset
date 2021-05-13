n, x = map(int, input().split())
M = []
ans = 0
for i in range(n):
    m = int(input())
    M.append(m)
M.sort()
now = 0
#print(M)
for i in range(n):
    now += M[i]
    if now > x:
        print(ans)
        exit()
    else:
        ans += 1
while True:    
    now += M[0]
    if now > x:
        print(ans)
        exit()
    else:
        ans += 1