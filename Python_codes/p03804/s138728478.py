n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]

flag = True
for i in range(n):
    if flag:
        for j in range(n):
            if i + m <= n and j + m <= n:
                aa = []
                for k in range(m):
                    aa.append(a[i + k][j : j+m])
                if aa == b:
                    print('Yes')
                    flag = False
                    break

if flag:
        print('No')