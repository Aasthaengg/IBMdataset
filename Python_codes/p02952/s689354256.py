N = int(input())

cnt = 0
for i in range(1, N+1):
    k = 0
    while True:
        k += 1
        if 10 ** k > i: break
    if k % 2 == 1:
        cnt += 1
print(cnt)
