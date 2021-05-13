N = int(input())
A = input().split()
R = []
L = []
for i,a in enumerate(A):
    if i%2 == 0:
        R.append(a)
    else:
        L.append(a)
ans = list(reversed(L))+R
if N%2 == 0:
    print(' '.join(ans))
else:
    print(' '.join(list(reversed(ans))))