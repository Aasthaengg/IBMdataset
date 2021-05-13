import math
cnt = 0
N = int(input())
for i in range(N):
    n = int(input())
    if n % 2:
        area = round(math.sqrt(n))
        prime_ng = 0
        for i in range(2, area + 1):
            if n % i == 0:
                prime_ng = 1
                break
        if prime_ng == 0:
            cnt += 1
    elif n == 2:
        cnt += 1
print(cnt)