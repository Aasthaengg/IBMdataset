import math

k = int(input())
gusu = math.floor(k/2)
kisu = math.ceil(k/2)

# n個からr個を選ぶ組み合わせを算出する
def combinations_count(n, r):
   return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = combinations_count(gusu,1)*combinations_count(kisu,1)
print(ans)