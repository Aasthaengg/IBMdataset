N = int(input())
S = str(input())

if N%2==1:
    print('No')
else:
    half = N//2
    for i in range(half):
        if S[i]!=S[i+half]:
            print('No')
            break
    else:
        print('Yes')