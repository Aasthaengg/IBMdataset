S = input()
for i in range(1, len(S) + 1):
    if (i % 2 == 1 and S[i - 1] == 'L'
    or i % 2 == 0 and S[i - 1] == 'R'):
        print('No')
        quit()
print('Yes')