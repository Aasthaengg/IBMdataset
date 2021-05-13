from collections import Counter

N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

D = Counter(D)
T = Counter(T)

for i in T:
    D_count = D[i]
    T_count = T[i]
    if T_count > D_count:
        print("NO")
        exit()
print("YES")