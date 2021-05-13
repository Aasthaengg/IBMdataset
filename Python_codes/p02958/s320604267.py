n = int(input())
p = list(map(int,input().split()))
q = []
for i in range(n):
    if p[i] == i+1:
        continue
    else:
        q.append(i)
if len(q) == 2 or len(q) == 0:
    print('YES')
else:
    print('NO')