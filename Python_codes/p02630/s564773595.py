from collections import Counter
n = int(input())
A = list(map(int, input().split()))
a = Counter(A)
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

ans = sum(A)
for b,c in bc:
    ans -= b*a[b]
    ans += c*a[b]
    if b in a:
        if c in a: a[c] += a[b]
        else: a[c] = a[b]
        a.pop(b)
    print(ans)