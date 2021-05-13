n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
a.sort(key = lambda x:x[1])
j = 0

for i in range(n):
    j += a[i][0]
    if j > a[i][1]:
        print('No')
        exit(0)

print('Yes')