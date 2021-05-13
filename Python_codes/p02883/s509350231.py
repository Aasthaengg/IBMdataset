n, k = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort(reverse=True)
F.sort()

def ok(x):
    tot = 0
    for i in range(n):
        tot += max(0, A[i] - x//F[i])
    if tot <= k:
        return True
    else:
        return False

l = -1
r = 10**18
while l+1 < r:
    c = (l+r)//2
    if ok(c):
        r = c
    else:
        l = c
print(r)