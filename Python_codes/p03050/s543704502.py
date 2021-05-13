N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


n = make_divisors(N)
answer = 0
for i in n[::-1]:
    if i == 1:
        continue
    q, r = divmod(N, i - 1)
    if q == r:
        answer += i - 1
    else:
        break

print(answer)