from collections import Counter
from operator import itemgetter

N,K = list(map(int,input().split()))
A = list(Counter(map(int,input().split())).items())
A = sorted(A,key=itemgetter(1),reverse = True)

ans = 0
B = A[K:]
for i in range(len(B)):
    ans += B[i][1]
print(ans)