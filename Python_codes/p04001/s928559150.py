s = input()

n = 2 ** (len(s) - 1)
result = 0

for i in range(n):
  bin_n = bin(i)[2:]
  bin_n = '0' * ((len(s) - 1) - len(bin_n)) + bin_n
  current_address = 0
  for j in range(len(bin_n)):
    if bin_n[j] == '1':
      result += int(s[current_address:j+1])
      current_address = j+1

  result += int(s[current_address:])

print(result)