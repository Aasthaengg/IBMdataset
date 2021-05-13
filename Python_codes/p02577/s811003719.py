n = int(input())
str_n = str(n)
sum = 0
for i in range(len(str(n))):
    sum += int(str_n[i])

if not sum % 9:
    print('Yes')
else:
    print('No')

