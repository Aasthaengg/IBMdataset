A, B, K = map(int, input().split())
cnt = 0
for i in range(1, 101)[::-1]:
    if A % i == B % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        exit()