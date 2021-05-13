S = input()
T = input()
t_len = len(T)
count = len(S) - len(T) + 1
max_correct = []
for i in range(count):
  s_tmp = S[i:t_len]
  correct = 0
  for n, s in enumerate(s_tmp):
    if s == T[n]:
      correct += 1
  max_correct.append(correct)
  
  i = i + 1
  t_len = t_len + 1

max_correct = len(T) - max(max_correct)
print(max_correct)