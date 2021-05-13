def prime_factor_2(n):
  if n % 2 == 0 and n % 4 != 0:
    return 1
  if n % 2 == 1:
    return 0
  
  return 1 + prime_factor_2(int(n/2))

N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
print(sum([prime_factor_2(a) for a in A]))