import sys
N = int(input())
S = input()

if N % 2 != 0:
    print('No')
    sys.exit(0)
else:
    idx = int(N/2)
    if S[:idx] == S[idx:]:
        print('Yes')
    else:
        print('No')