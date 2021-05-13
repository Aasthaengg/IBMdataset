A,B,C = map(int,input().split())
K = int(input())
for _ in range(K):
    if A >= B :
        B = B*2
        continue
    elif B >= C:
        C = C*2
        continue
if A < B and B < C:
    print('Yes')
else:
    print('No')
