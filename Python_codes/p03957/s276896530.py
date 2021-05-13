s = input()
flag = False
if 'C' in s and 'F' in s and s.index('C') < s.rindex('F'):
  flag = True
print('Yes' if flag == True else 'No')
