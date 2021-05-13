N = int(input())
la = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if la[i] % 2 == 0:
        cnt += 1

print(3**N - 2**cnt)