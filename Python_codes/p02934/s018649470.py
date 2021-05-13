n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += pow(a[i], -1)
print(pow(ans, -1))