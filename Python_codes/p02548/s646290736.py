N = int(input())
cnt = 0
for i in range(1, N):
    cnt += N // i
    if N % i == 0:
        cnt -= 1
print(cnt)
