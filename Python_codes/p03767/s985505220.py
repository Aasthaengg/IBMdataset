n = int(input())
la = [int(w) for w in input().split()]
la.sort()
ans = 0
for i in range(1, n+1):
    ans += la[-2 * i]
print(ans)
