N = int(input())
import collections

def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i - 1 <= i:
                continue
            divisors.append(n // i)
            # if i != n // i:
            #     divisors.append(n // i)

    # divisors.sort()
    return divisors

div = make_divisors(N)

# print(collections.Counter(div))
# print(div)
print(sum(div)-len(div))