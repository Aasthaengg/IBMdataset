N = input()
NN = []
for i in range(len(N)):
    if N[i] == '9':
        NN.append('1')
    elif N[i] == '1':
        NN.append('9')
print(''.join(NN))