def d_2_c(n):
  a = 0
  while(n % 2 == 0):
    n = int(n/2)
    a += 1
  return a

N = input()
print(min(list(map(lambda a: d_2_c(int(a)), input().split(" ")))))