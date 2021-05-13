N,A,B,C,D = map(int,input().split())
S = ['#']+list(input())
CanReach = True
CanChange = False
for i in range(A,C):
    if S[i] == '#' and S[i+1] == '#':
        CanReach = False
for i in range(B,D):
    if S[i] == '#' and S[i+1] == '#':
        CanReach = False
if C < D:
    CanChange = True
else:
    for i in range(B,D+1):
        if S[i-1] == '.' and S[i] == '.' and S[i+1] == '.':
            CanChange = True
if CanReach and CanChange:
    print('Yes')
else:
    print('No')