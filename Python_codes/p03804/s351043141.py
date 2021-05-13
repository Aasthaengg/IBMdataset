n, m = map(int, input().split())
A = [str(input()) for _ in range(n)]
B = [str(input()) for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        for x in range(m):
            for y in range(m):
                if A[j+y][i+x] != B[y][x]:
                    break
            else:
                continue
            break
        else:
            print('Yes')
            exit()
else:
    print('No')
