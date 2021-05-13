a, b, k = [int(x) for x in input().split()]

divisors = []
for x in range(1, max(a, b)+1):
  if a % x == 0 and b % x == 0:
    divisors.append(x)

divisors.reverse()
print(divisors[k-1])