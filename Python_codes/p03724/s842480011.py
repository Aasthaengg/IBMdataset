n,m = map(int,input().split())

l = [0]*n #l[i]: i~i+1

for _ in range(m):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    l[a-1] += 1
    l[b-1] += -1

for i in range(1,n):
    l[i] += l[i-1]

if all(x%2 == 0 for x in l):
    print('YES')
else:
    print('NO')