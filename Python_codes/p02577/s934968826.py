l = list(map(int, input()))
sum = 0
for i in range(len(l)):
    sum += l[i]

print('Yes' if sum % 9 == 0 else 'No')