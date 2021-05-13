n = int(input())
jp, bit = 0, 0
for i in range(n):
  a, b = input().split()
  if b == "JPY":
    jp += float(a)
  else:
    bit += float(a)
print(jp+380000*bit)