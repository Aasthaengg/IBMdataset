
N = int(input())

C = []

for i in range(N):

    c = int(input())

    if len(C) == 0 or C[-1] != c-1:
        C.append(c-1)

lis = []
last = [-1] * (2 * (10**5))

for i in range(len(C)):

    if i == 0:
        lis.append(1)
    
    elif last[C[i]] == -1 or last[C[i]] == i-1:
        lis.append(lis[-1])

    else:
        lis.append(lis[-1]+lis[last[C[i]]])

    lis[-1] %= 10 ** 9 + 7
    last[C[i]] = i


print (lis[-1])
