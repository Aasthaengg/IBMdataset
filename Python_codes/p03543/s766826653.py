s = input()
front = len(set(s[:3])) == 1
back = len(set(s[1:])) == 1
  
print('Yes' if front or back else 'No')