def calc(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


N = int(input())

answer = None

for i in range(1, N):
    A = i
    B = N - i

    C = calc(A) + calc(B)

    if answer is None or answer > C:
        answer = C

print(answer)
