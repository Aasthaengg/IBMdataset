from collections import Counter

N = int(input())
al = list(map(int,input().split()))
C = Counter(al)

ans = 0
for i in C.keys():
    if i in C:
        if C[i] == i:
            continue
        elif C[i] > i:
            ans += C[i] - i
        else:
            ans += C[i]
print(ans)