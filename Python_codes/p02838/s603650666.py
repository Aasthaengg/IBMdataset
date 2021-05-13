n = int(input())
str_a = ''.join(['{:060b}'.format(a) for a in map(int, input().split())])
mod = 10**9 + 7

rest = 0
for d in range(60):
  ones = str_a[59-d::60].count('1')
  rest = (rest + 2**d * ones * (n - ones)) % mod
    
print(rest)
