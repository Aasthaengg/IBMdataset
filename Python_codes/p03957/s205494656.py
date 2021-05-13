S = input()
num = 0
for i in range(len(S)):
    if num == 0 and S[i] == 'C':
        num += 1
    if num == 1 and S[i] == 'F':
        print('Yes')
        exit()

print('No')
