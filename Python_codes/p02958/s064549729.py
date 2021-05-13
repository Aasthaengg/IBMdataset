n = int(input())
q = range(1,n+1)
p = list(map(int,input().split()))
if 2 >= sum(p[i] != q[i] for i in range(n)):
    print('YES')
else:
    print('NO')
