def calc_sum_digits(n):
    return sum(int(x) for x in str(n))

N, A, B = map(int, input().split())
print(sum(n if A <= calc_sum_digits(n) <= B else 0 for n in range(1, N+1)))