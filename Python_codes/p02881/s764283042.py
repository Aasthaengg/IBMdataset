N = int(input())

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

ans = make_divisors(N)
result = []
if len(ans)%2 == 0:
    for i, j in zip(range(0, int(len(ans)/2)), reversed(range(int(len(ans)/2), len(ans)))):
        result.append(int(ans[i]+ans[j])-2)
else:
    x = ans[int(len(ans)/2)]
    result.append((x-1)*2)
print(min(result))