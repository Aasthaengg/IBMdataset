num_list = input().split(' ')
N = int(num_list[0])
A = int(num_list[1])
B = int(num_list[2])
total = 0
for n in range(N+1):
  calc_num = 0
  for s in str(n):
    calc_num += int(s)
  if A <= calc_num <= B:
    total += n
print(total)