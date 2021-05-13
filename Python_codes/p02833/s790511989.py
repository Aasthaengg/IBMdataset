N = int(input())
n = N // 10
cnt = 0
if N % 2 == 0:
    while n != 0:
        cnt += n
        n //= 5
print(cnt)