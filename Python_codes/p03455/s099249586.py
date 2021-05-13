import sys

input_list = sys.stdin
for num in input_list:
  num_list = num.split(' ')
a = int(num_list[0]) % 2
b = int(num_list[1]) % 2
ans = 'Even'
if a * b == 1:
  ans = 'Odd'
print(ans)