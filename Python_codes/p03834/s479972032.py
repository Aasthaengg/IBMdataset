s = input()
s2 = list(s)

s2[5] = " "
s2[13] =" "

for i in range(len(s2)):
    print(s2[i], end='')