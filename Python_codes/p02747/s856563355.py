S = input()
n = len(S)
if n % 2 == 1:
    print('No')
    exit()
for i in range(0, n, 2):
    if S[i:i+2] != 'hi':
        print('No')
        break
else:
    print('Yes')