S = input()
T = input()

if T.startswith(S) == True:
    if len(S)+1 == len(T):
        print('Yes')
    else:
        print('No')
else:
    print('No')

