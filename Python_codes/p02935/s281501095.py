n = int(input())
v = list(map(float, input().split()))
v.sort()

for _ in range(n-1):
    v[1] = (v[0]+v[1])/2
    v.pop(0)
print(v[0])