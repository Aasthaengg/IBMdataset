def is_fizz(n):
  return True if (n % 3 == 0) else False

def is_buzz(n):
  return True if (n % 5 == 0) else False

def is_fizzbuzz(n):
  return True if (n % 3 == 0 and n % 5 == 0) else False

N = int(input())
sum = 0
for n in range(1, N + 1):
  if not is_fizz(n) and not is_buzz(n) and not is_fizzbuzz(n):
    sum += n
print(sum)