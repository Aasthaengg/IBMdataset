N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))
D.sort()
T.sort()
j = 0
for i in range(M):
    while j < N:
        if D[j] == T[i]:
            break
        j += 1
    if j == N:
        print('NO')
        exit()
    j += 1
print('YES')
