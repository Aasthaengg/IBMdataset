N_list = [int(i) for i in list(input())]
N_list = N_list[::-1] + [0]

for index in range(0, len(N_list)):
  if N_list[index] >= 6 or (N_list[index] == 5 and N_list[index+1] >= 5) :
    N_list[index] = 10 - N_list[index]
    N_list[index+1] += 1

print(sum(N_list))