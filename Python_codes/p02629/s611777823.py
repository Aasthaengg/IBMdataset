n = int(input())
n -= 1
n_26 = []

while n>=0:
  n_26.append(n%26)
  n //= 26
  n -= 1

name = map(lambda x:chr(x+97),n_26[::-1])
print(''.join(name))