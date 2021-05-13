N,M = (int(x) for x in input().split())
if N == 1:
    if M == 1:
        print('1')
    elif M == 2:
        print('0')
    else:
        print(M-2)
elif M == 1:
    if N == 2:
        print('0')
    else:
        print(N-2)
else:
    print((N-2)*(M-2))