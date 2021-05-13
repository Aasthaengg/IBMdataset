s = input()

sum = 0
tmp = 2 ** (len(s) -1)

for i in range(tmp):
    format_spec = '0{}b'.format(len(s)-1)
    flag = format(i, format_spec)
    my_sum = 0
    before = 0
    for j in range(len(s) - 1):
        if flag[j] == '1':
            my_sum += int(s[before:j+1])
            before = j+1
    my_sum += int(s[before:])
    sum += my_sum

print(sum)