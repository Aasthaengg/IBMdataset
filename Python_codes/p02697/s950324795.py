N, M = map(int, input().split())

ans = []

for i in range(M):
    if N % 2 != 0 or (M + (i + 1)) - (M - (i)) < N // 2:
        tmp = [str(M - (i)), str(M + (i + 1))]
    else:
        tmp = [str(M - (i)), str(M + (i + 2))]
    tmp = ' '.join(tmp)
    ans.append(tmp)
print(*ans, sep='\n')
