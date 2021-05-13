input_value = raw_input().split(' ')
ret = 'a == b'
if int(input_value[0]) < int(input_value[1]): ret = 'a < b'
if int(input_value[0]) > int(input_value[1]): ret = 'a > b'
print(ret)