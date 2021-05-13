N = int(input())

exp_2_list = []
for i in range(100):
  exp_2 = 2 ** i
  if exp_2 > 100:
    break
  exp_2_list.append(exp_2)

answer = 1
for exp_2 in sorted(exp_2_list, reverse=True):
  if exp_2 <= N:
    answer = exp_2
    break

print(answer)