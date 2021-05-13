s = input()
c = 0
i = 0
test = 'CODEFESTIVAL2016'
for k in s:
    if k != test[i]:
        c += 1
    i += 1

print(c)         
