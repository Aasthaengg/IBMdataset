N, A, B, C, D = map(int, input().split())
S = input()

s = A
f = B
flag = True
if C < D:
    if '##' in S[A-1:C]:
        flag = False
    if '##' in S[B-1:D]:
        flag = False

else:
    if S[D - 2] == '#':
        if '...' not in S[B-2:D]:
            flag = False
    if '##' in S[A-1:C]:
        flag = False
ans = 'Yes' if flag else 'No'
print(ans)