N, M, K = map(int, input().split())

# nは行で押したボタンの数、mは列で押したボタンの数。
for n in range(N+1):
    for m in range(M+1):
        if n * (M - m) + m * (N - n) == K:
            print("Yes")
            exit()
else:
    print("No")