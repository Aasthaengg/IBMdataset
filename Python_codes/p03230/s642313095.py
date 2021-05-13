N = int(input())
a = [[ i*(i+1)//2 + j + 1 for j in range(i+1)] for i in range(540)]

k = 1
while k*(k-1)//2 < N:
    k += 1

if k*(k-1)//2 == N:
    print('Yes')
    print(k)
    for i in range(k-1):
        print(str(k-1), end='')
        for j in range(i+1):
            print(' '+str(a[i][j]), end='')
        for j in range(i+1, k-1):
            print(' '+str(a[j][i]), end='')
        print('')
    print(str(k-1), end='')
    for i in range(k-1):
        print(' '+str(a[i][i]), end='')
    print('')
else :
    print('No')