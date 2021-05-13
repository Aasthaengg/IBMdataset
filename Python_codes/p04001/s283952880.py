S = input()
N = len(S)
Sum = 0
for i in range(2**(N-1)):
    exp = []
    for j in range(N):
        exp.append(S[j])
        if ((i >> j) & 1):
            exp.append('+')
    
    a = ''
    for j in range(len(exp)):
        if exp[j] == '+':
            Sum += int(a)
            a = ''
        else:
            a += exp[j]
        if j == (len(exp)-1):
            Sum += int(a)
    
print(Sum)