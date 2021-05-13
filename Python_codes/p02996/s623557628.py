n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
L = sorted(l, key = lambda x:x[1])
cumsum = 0
for i in range(n):
    cumsum += L[i][0]
    if cumsum > L[i][1]:
        print('No')
        exit()
print('Yes')