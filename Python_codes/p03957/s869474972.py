s=input()
f='C' in s and 'F' in s and s.index('C')<len(s)-1-s[::-1].index('F')
print('Yes' if f else 'No')