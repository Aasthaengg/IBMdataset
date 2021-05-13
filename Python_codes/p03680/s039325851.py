N = int(input())
num = 0
index = 0
a_lst = []
for _ in range(N):
  a_lst.append(int(input()))
past_index = [0] * N
while True:
  num += 1
  index = a_lst[index]-1
  if index == 1:
    break
  elif past_index[index] == 1:
    num = -1
    break
  else:
    past_index[index] = 1
print(num)