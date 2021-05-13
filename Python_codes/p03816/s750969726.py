from collections import Counter

N = int(input())
A = list(map(int,input().split()))
A.sort()
#print(A)

Ac = Counter(A).most_common()
#print(Ac)
ans = 0

for i in range(len(Ac)):
    if Ac[i][1] > 1:
        ans += Ac[i][1]-1

print(N-ans if ans%2 == 0 else N-ans-1)
