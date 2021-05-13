s = input()
code = 'CODEFESTIVAL2016'
count = 0

for i in range(16):
    if s[i] != code[i]:
        count += 1

print(count)