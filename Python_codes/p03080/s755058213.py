num = int(input())
seq = input()
num_R = seq.count('R')
if num_R > num // 2:
  print('Yes')
else:
  print('No')
