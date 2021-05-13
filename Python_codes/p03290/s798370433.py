d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

n = 2 ** d
result = 100 * 10

for i in range(n):
  bin_n = bin(i)[2:]
  bin_n = '0' * (d - len(bin_n)) + bin_n
  max_address = -1
  total = 0
  num_of_question = 0

  for j in range(d):
    if bin_n[j] == '1':
      total += (j+1) * 100 * pc[j][0] + pc[j][1]
      num_of_question += pc[j][0]
    
    else:
      max_address = j
  
  if total >= g:
    result = min(result, num_of_question)
  
  else:
    for _ in range(pc[max_address][0]):
      num_of_question += 1
      total += (max_address+1) * 100
      if total >= g:
        result = min(result, num_of_question)
        break

print(result)