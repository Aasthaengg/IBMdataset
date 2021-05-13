N = input()
for i in range(10):
    if N.count(str(i)*3):
        print('Yes')
        exit()
print('No')
