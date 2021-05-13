N = int(input())
A = list(map(int, input().split()))

minus = 0

for a in A:
    if a < 0:
        minus += 1


ans = 0
minA = float('inf')
for a in A:
    ans += abs(a)
    if minA > abs(a):
        minA = abs(a)

if 0 in A or minus % 2 == 0:
    print(ans)
    exit(0)

ans -= 2 * minA
print(ans)
