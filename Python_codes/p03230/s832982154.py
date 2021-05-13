# D - Crossing
N = int(input())
k = 1

def list_print(S):
    print(len(S), end='')
    for i in range(len(S)):
        print(' {}'.format(S[i]), end='')
    print('')

while k<1000:
    if k*(k-1)//2==N:
        break
    k += 1
if k==1000:
    print('No')
else:
    S = [[] for _ in range(k)]
    i = 1
    for l in range(k):
        for r in range(l+1,k):
            S[l].append(i)
            S[r].append(i)
            i += 1
    print('Yes')
    print(k)
    for i in range(k):
        list_print(S[i])