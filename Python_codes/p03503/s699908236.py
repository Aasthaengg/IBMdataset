n = int(input())
list_F = [ list(map(int,input().split(" "))) for i in range(n)]
list_P = [ list(map(int,input().split(" "))) for i in range(n)]
ans = (-1)*pow(10, 9)
a = 0
for i in range(1, 2**10):
    value = 0
    for k in range(n):
        l = list_F[k]
        cnt = 0
        for j in range(10):
            if ((i >> j) & 1):
                if l[j] == 1:
                    cnt += 1
        value += list_P[k][cnt]
    ans = max(ans, value)

print(ans)