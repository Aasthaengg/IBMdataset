s = input()
m = 0
temp = 0
for i in range(3):
    if s[i] == 'R':
        temp += 1
        if temp > m:
            m = temp
    else:
        if temp > m:
            m = temp
        temp = 0
print(m)