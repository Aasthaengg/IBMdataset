b ='CODEFESTIVAL2016'

a = input()

count = 0
for i in range(16):
    if a[i] != b[i]:
        count += 1
print(count)