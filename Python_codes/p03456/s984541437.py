a,b = input().split()
print('Yes' if str(int(a+b)**0.5)[-1] == '0' else 'No')