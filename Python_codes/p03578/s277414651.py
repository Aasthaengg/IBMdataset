n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
d.sort()
t.sort()
j = 0
for i in range(n):
    if d[i] == t[j]:
        j += 1
    if j == m:
        break

if j == m:
    print('YES')
else:
    print('NO')