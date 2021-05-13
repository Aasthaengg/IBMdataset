N = int(input())

cnt = 0
for i in range(N):
    num = len(str(N-i))
    if num % 2 != 0:
        cnt += 1
print(cnt)