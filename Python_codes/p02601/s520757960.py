A, B, C = map(int, input().split())
K = int(input())

for _ in range(K):
    if A >= B:
        B *= 2
    elif B >= C:
        C *= 2
    else:
        C *= 2

if (B > A) and (C > B):
    print ('Yes')
else:
    print ('No')