S = input()
N = len(S)
for i in range(2**(N-1)):
    sum = int(S[0])
    f = S[0]
    for j in range(N-1):
        if (i >> j) & 1:
            f += '+'
            sum += int(S[j+1])
        else:
            f += '-'
            sum -= int(S[j+1])
        f += S[j+1]
    # calc
    if sum == 7:
        print('{}=7'.format(f))
        break
