n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(n):
    v[i] -= c[i]
print(sum(x for x in v if x > 0))