# D. Partition
# https://atcoder.jp/contests/abc112/tasks/abc112_d

# 約数列挙

def make_divisors(n):
    lower_divisors = []
    upper_divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)

    upper_divisors.reverse()
    return lower_divisors + upper_divisors

n, m = map(int, input().split())

box = make_divisors(m)

for i in range(len(box)):
  if box[i] >= n:
    print(m // box[i])
    exit()
