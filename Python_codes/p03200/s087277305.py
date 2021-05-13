from collections import Counter

S = input()
s_list = []
for i, s in enumerate(S):
  if s == 'W':
    s_list.append(i)
t_list = [i for i in range(len(s_list))]
answer = 0
for i in range(len(s_list)):
  answer += s_list[i] - t_list[i]
print(answer)

