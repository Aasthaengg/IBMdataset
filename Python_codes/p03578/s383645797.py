n = int(input())
D = list(map(int,input().split()))
m = int(input())
T = list(map(int,input().split()))

p = {}
for d in D:
    if d not in p:
        p[d] = 1
    else:
        p[d] += 1

for t in T:
    if t not in p:
        print('NO')
        exit()
    if p[t] == 0:
        print('NO')
        exit()
    p[t] -= 1
    
print('YES')