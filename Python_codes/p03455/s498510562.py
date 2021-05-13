a, b = map(int, input().split())
c = int(a * b)
def f(n):
  if n % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
print(f(c))