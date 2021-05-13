from collections import defaultdict
import math


N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

nums = make_divisors(N)
# print(nums)
ans = 0
for num in nums:
    if num != 1:
        if N % (num -1) == N // (num -1):
            ans += num -1
print(ans)
# for m in range(1,N + 1):
#     ans = 0
#     if N//m == N % m:
#         print("SAME")
#         print(f"{m}: 商:{N//m} 余り:{N % m}")
#         print("SAME")