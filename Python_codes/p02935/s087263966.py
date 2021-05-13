N = int(input())
v = list(map(int, input().split()))
v.sort()
for i in range(N-1):
    v[0] = (v[0]+v[1])/2
    v.pop(1)
print(*v)