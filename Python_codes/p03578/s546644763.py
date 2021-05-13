n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))

d.sort()
t.sort()
j = 0
#print(d)
#print(t)
for i in range(n):
    if d[i] == t[j]:
        if j < m-1:
            j += 1
        else:
            j += 1
            break

if j == m:
    print('YES')
else:
    print('NO')