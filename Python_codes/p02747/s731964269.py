S = input()
if len(S)%2:
    print('No')
    exit()

for i in range(len(S)//2):
    if S[2*i:2*i+2] != 'hi':
        print('No')
        exit()

print('Yes')
