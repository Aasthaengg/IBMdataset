import itertools

n = int(input())
D = list(map(int, input().split()))

l1 = [x for x in range(n)]
l2 = [x for x in range(n)]

ans = 0
sub = 0

for v1, v2 in itertools.product(l1, l2):
    ans += D[v1] * D[v2]

for i in range(n):
    sub += D[i]*D[i]

print((ans-sub)//2)