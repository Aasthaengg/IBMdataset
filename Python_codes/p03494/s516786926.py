N = int(input())
A = list(map(int, input().split()))
ans = 0
isEnd = False
while not isEnd:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] // 2
        else:
            isEnd = True
            break
    if not isEnd:
        ans += 1
print(ans)
