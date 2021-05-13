import copy

def check(arr, val):
    for i in arr:
        if not i == val:
            return False
    return True

n, k = map(int, input().split())
a = [int(_) for _ in input().split()]

for _ in range(k):
    aa = [0] * n
    for i in range(n):
        aa[max(0, i-a[i])] += 1
        r = i+a[i]+1
        if r < n:
            aa[r] -= 1
    for i in range(1, n):
        aa[i] += aa[i-1]
    a = aa.copy()
    if check(a, n):
        break

for i in a:
    print(i, end=' ')
print()