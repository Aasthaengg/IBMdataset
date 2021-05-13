# ABC078 C HSI

n, m = map(int, input().split())

i = (1/2)**m

x = (100*(n-m) + 1900*m) / i
print(int(x))