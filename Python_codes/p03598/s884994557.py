n = int(input())
k = int(input())
X = [int(i) for i in input().split()]

ans = 0
for x in X:
    dis_a = x
    dis_b = abs(k - x)
    ans += min(dis_a, dis_b) * 2
print(ans)