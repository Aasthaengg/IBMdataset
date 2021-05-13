import math

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
divisors_list = make_divisors(n)
ans = []
n_sqrt = math.sqrt(n)
if n_sqrt == int(n_sqrt):
    for i in range(len(divisors_list) // 2 + 1):
        move = divisors_list[i] + divisors_list[-1 - i] - 2
        ans.append(move)
else:
    for i in range(len(divisors_list) // 2):
        move = divisors_list[i] + divisors_list[-1 - i] - 2
        ans.append(move)
print(min(ans))
