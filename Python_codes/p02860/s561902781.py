N = int(input())
if N%2==1:
    print('No')
else:
    S = input()
    SF = S[:N//2]
    SS = S[N//2:]
    if SF==SS:
        print('Yes')
    else:
        print('No')