n = int(raw_input())
s = ''

for i in range(1, n+1):
    if i%3 == 0:
        s = s + ' ' + str(i)
    else:
        temp = ''
        temp = str(i)
        for j in range(len(temp)):
            if temp[j] == '3':
                s = s + ' ' + str(i)
                break
print s