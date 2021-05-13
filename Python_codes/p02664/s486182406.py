str = input()
str = list(str)


for index, value in enumerate(str):
    if (value == '?' and index == len(str) - 1):
        str[index] = 'D'

    elif (value == '?' and index != 0 and str[index - 1] == 'P'):
        str[index] = 'D'

    elif (value == '?' and str[index + 1] == '?'):
        str[index] = 'P'
        str[index + 1] = 'D'
    elif (value == '?'):
    	str[index] = 'D'


print(''.join(str))