n = int(input())
v = list(map(int, input().split()))
v.sort()
ans = 0
for i in range(n-1):
    a = (v[i]+v[i+1])/2
    ans += a
    v[i], v[i+1] = 0,a
print(v[-1])