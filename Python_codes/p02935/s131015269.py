n = int(input())
v = sorted(map(int, input().split()))
prev = v[0]
for i in range(1,n) :
    ans = (v[i] + prev) / 2
    prev = ans
print(ans)
