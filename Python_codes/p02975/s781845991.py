from collections import Counter

N = int(input())
A = list(map(int,input().split()))

c = Counter(A)

t = 0
for a in A:
    t ^= a

if c[0] == N:
    print('Yes')
elif N % 3 == 0:
    if c[0] == int(N//3) and len(c) == 2:
        print('Yes')
    elif len(c) == 3 and t == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')