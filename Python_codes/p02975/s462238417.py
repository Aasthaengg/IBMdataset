from collections import Counter

N = int(input())

A = list(map(int, input().split()))
c = Counter(A)
a = list(set(A))


if len(a) >= 4:
    ans = False

elif len(a) == 3:
    a, b, d = a
    if c[a] == c[b] and c[b] == c[d] and a^b == d and d^b == a and a^d == b:
        ans = True
    else:
        ans = False

elif len(a) == 2:
    a, b = sorted(a)
    if a == 0 and c[a] == N/3 and c[b] == (N/3)*2:
        ans = True
    else:
        ans = False

elif len(a) == 1:
    if sum(a) == 0:
        ans = True
    else:
        ans = False

print("Yes" if ans else "No")
