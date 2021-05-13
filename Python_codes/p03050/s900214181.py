N = int(input())

def divisors(n):
  divisors = set()
  for i in range(1, int(n**0.5)+1):
    if n%i == 0:
      divisors.add(n//i)
  return divisors

ans = 0
for i in divisors(N):
  if i - 1 > N//i:
    ans += i - 1
print(ans)