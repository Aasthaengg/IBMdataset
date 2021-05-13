def solve(a, b):
    v = [0,0,0,0]
    for i in range(3):
        v[a[i]-1] += 1
        v[b[i]-1] += 1
    return "YES" if sorted(v) == [1,1,2,2] else "NO"

a = [0]*3
b = [0]*3
for i in range(3):
    a[i], b[i] = map(int, input().split())
print(solve(a, b))