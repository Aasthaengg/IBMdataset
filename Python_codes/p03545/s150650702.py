abcd = str(input())
ans = ''

for i in range(2**(len(abcd)-1)):
  total = int(abcd[0])
  ans = abcd[0]
  for j in range(len(abcd)-1):
    if (i >> j) & 1:
      total += int(abcd[j+1])
      ans = ans + '+' + abcd[j+1]
    else:
      total -= int(abcd[j+1])
      ans = ans + '-' + abcd[j+1]
  if total == 7:
    ans = ans + '=7'
    break
print(ans)