n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

ok = [[0 for i in range(2001)] for j in range(21)]
ok[0][0] = 1

for i in range(n):
    for j in range(2001):
        if j+a[i] > 2000:
            ok[i+1][j] = max(ok[i][j], ok[i+1][j])
        else:
            ok[i+1][j] = max(ok[i][j], ok[i+1][j])
            ok[i+1][j+a[i]] = max(ok[i][j], ok[i+1][j+a[i]])

for i in m:
    print('yes' if ok[n][i] else 'no')
