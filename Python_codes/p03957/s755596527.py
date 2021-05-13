s = input()
print("Yes" if 'C' in s and 'F' in s and s.find('C') < s.rfind('F') else "No")