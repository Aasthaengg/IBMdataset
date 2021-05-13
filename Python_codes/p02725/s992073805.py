k, n = map(int, input().split())
A = list(map(int, input().split()))

dist = 0
ng = 0
for i in range(n-1):
    sub = A[i+1] - A[i]
    if sub > ng:
        ng = sub
    dist += sub

sub = A[0] + (k - A[-1])
if sub > ng:
    ng = sub
dist += sub

print(dist - ng)