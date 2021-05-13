S = input()

for i in range(1, len(S)+1):
    if i % 2 == 0 and S[i-1] == 'R':
        print('No')
        break
    elif i % 2 != 0 and S[i-1] == 'L':
        print('No')
        break
else:
    print('Yes')
