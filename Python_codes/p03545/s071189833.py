s = list(input())

for i in range(3**2):
    number = int(s[0])
    str = s[0]
    for j in range(3):
        if ((i>>j)&1):
            number += int(s[j+1])
            str += '+'+s[j+1]
        else:
            number -= int(s[j+1])
            str += '-'+s[j+1]
    if number == 7:
        print(str + '=7')
        exit(0)