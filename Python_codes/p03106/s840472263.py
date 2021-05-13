a, b, k = map(int, input().split())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a_y = set(make_divisors(a))
b_y = set(make_divisors(b))
#print(a_y & b_y)
y = list(a_y & b_y)
y.sort(reverse=True)
print(y[k-1])

