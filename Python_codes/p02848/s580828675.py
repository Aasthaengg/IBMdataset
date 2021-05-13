n = int(input())
s = input()

m = map(
  lambda x: chr((ord(x) - ord('A') + n) % 26 + ord('A')), list(s))
print(''.join(list(m)))
