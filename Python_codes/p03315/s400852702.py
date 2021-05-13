tmp = input()
sum = 0
for i in range(4):
    if tmp[i] == '+':
        sum += 1
    else:
        sum -= 1
print(sum)