N, M = list(map(int,input().split()))
s = [0]*M
c = [0]*M
for i in range(M):
    s[i], c[i] = list(map(int,input().split()))
    s[i] -= 1

err = False

digit = [0]*N
digit_bool = [False]*N

for i in range(M):
    if digit_bool[s[i]]:
        if digit[s[i]] != c[i]:
            err = True
    else:
        digit[s[i]] = c[i]
        digit_bool[s[i]] = True

if digit[0] == 0:
    if digit_bool[0]:
        if N != 1:
            err = True
    elif N == 1:
        digit[0] = 0
    else:
        digit[0] = 1

if err:
    print('-1')
else:
    print(''.join(list(map(str,digit))))