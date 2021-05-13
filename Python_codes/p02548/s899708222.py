n = int(input())

answer = 0

for i in range(1, n):
    if n % i == 0:
        answer += (n / i) - 1
    else:
        answer += n // i

print(int(answer))