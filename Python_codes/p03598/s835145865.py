n = int(input())
k = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    left = x*2
    right = abs(k-x)*2
    ans += min(left, right)
print(ans)
