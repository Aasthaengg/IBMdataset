N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

sum_A = sum(A)
d_candidate = make_divisors(sum_A)

for d in d_candidate:
    R = [a % d for a in A]
    R.sort()
    sum_R = sum(R)

    X, mod = divmod(sum_R, d)
    if mod != 0:
        continue

    if sum(R[:N-X]) <= K and (X * d - sum(R[-X:])) <= K:
        print(d)
        break
