def pop_count(n):
    return sum(n >> i & 1 for i in range(n.bit_length()))


def f(n):
    if n == 0:
        return 0
    return f(n % pop_count(n)) + 1


N = int(input())
X = input()
p = X.count("1")
rem_plus = 0
rem_minus = 0
for i in range(N):
    k = N - i - 1
    if X[i] == "0":
        continue
    elif p > 1:
        rem_minus = (rem_minus + pow(2, k, p - 1)) % (p - 1)
    rem_plus = (rem_plus + pow(2, k, p + 1)) % (p + 1)
for i in range(N):
    k = N - i - 1
    if X[i] == "0":
        print(f((rem_plus + pow(2, k, p + 1)) % (p + 1)) + 1)
    elif p > 1:
        print(f((rem_minus - pow(2, k, p - 1)) % (p - 1)) + 1)
    else:
        print(0)
