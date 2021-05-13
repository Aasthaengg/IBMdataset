num = list(str(input()))
num = [int(x) for x in list(num)]
print('Yes' if sum(num) % 9 == 0 else 'No')