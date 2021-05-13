berb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

S = list(input())

for i in range(len(S)):
    S[i] = berb.index(S[i])

S_d = [-1]
S_0 = len(S)
k = 0

while True:
    if k == 26:
        if len(S) == 0:
            print(-1)
            break
        else:
            S_d.append(S.pop(-1))
            k = 0
    elif k in S or k <= S_d[-1]:
        k += 1
    else:
        S.append(k)
        for j in range(len(S)):
            S[j] = berb[S[j]]

        print(''.join(S))
        break