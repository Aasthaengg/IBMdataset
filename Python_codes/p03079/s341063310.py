input_length = input().split(' ')

result = ''
x = input_length.count(input_length[0])
if x == len(input_length):
    print('Yes')
else:
    print('No')
  