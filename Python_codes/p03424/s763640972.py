import sys
N = int(input())
S = list(input().split())
if not ( 1 <= N <= 100 ):
    sys.exit()
for I in range(len(S)):
    if not (S[I] == 'P' or 'W' or 'G' or 'Y'):
        sys.exit()

result = set(S)
if len(result) == 3:
    print('Three')
else:
    print('Four')