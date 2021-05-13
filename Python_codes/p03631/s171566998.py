N = input()
for i in range(3):
    if N[i] != N[-i-1]:
        print('No')
        exit()
print('Yes')