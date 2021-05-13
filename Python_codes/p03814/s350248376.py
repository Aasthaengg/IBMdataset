s = input()
start_i, end_i = 0, 0
a_flag = True

for i, c in enumerate(s):
  if c == 'A' and a_flag:
    start_i = i
    a_flag = False
  if c == 'Z':
    end_i = i
    
print(end_i - start_i + 1)
