S = list(map(str,input()))

odd = ['R','U','D']
even = ['L','U','D']

for i in range(len(S)):
    if (i+1)%2 == 0:
        if S[i] in 'R':
            print('No')
            exit()
    elif (i+1)%2 == 1:
        if S[i] in 'L':
            print('No')
            exit()
print('Yes')