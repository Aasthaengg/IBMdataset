A, B, K = map(int, input().split())

def make_div(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  return divisors

print(sorted(set(make_div(A))&set(make_div(B)), reverse=True)[K-1])