n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
if any(a[i] == a[i+1] for i in range(n-1)):
    print('NO')
else:
    print('YES')
