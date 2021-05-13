N = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
val = 0
for i in range(N):
    if v[i] - c[i] > 0:
       val += v[i] - c[i]
print(val)
