s = input()
c = s.find('C')
print('Yes' if s.rfind('F') > c and c != -1 else 'No')
