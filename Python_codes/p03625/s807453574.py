from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]

A = Counter(a)
a_sorted = sorted(A.keys(), reverse=True)

ans = 0
tmp = 0
for i in a_sorted:
    if A[i] >= 4 and tmp == 0:
        ans = i**2
        break
    elif A[i] >= 2 and tmp == 0:
        tmp = i
    elif A[i] >= 2 and tmp != 0:
        ans = tmp * i
        break
print(ans)

