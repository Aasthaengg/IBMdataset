import sys
n = list(input())
int_n = int(''.join(n))
if not (111 <= int_n <= 999):
    sys.exit()

result = []
for I in n:
    if I == '1':
        result.append('9')
    elif I == '9':
        result.append('1')
    else:
        result.append(I)
print(int(''.join(result)))