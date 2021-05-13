N,K=list(map(int,input().split()))
A=list(map(int,input().split()))

from collections import Counter
A_ = Counter(A).most_common()[::-1]

ans=0
for _ in A_[:len(A_)-K]:
    if len(A_)-K <= 0:
        break
    ans += _[1]
    
print(ans)