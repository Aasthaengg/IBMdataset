#
A = input()
a_len = len(A)

answer = 0
for i in range(2**(a_len-1)):
  a_tmp = A
  total = 0
  bin_index = format(i, 'b').zfill(a_len-1)
  for j in range(a_len-1):
    a_tmp = list(a_tmp)
    if bin_index[j] == '1':
      a_tmp.insert(2*j+1, '+')
    else:
      a_tmp.insert(2*j+1, '#')
    a_tmp = ''.join(a_tmp)
  a_tmp = a_tmp.replace('#', '')
  a_tmp = map(int, a_tmp.split('+'))
  answer += sum(a_tmp)
print(str(answer))