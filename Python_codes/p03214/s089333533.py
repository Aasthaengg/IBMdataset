n = int(input())
a = list(map(int, input().split()))

# 平均を出す
mean = sum(a)/n

# 差分を求める
a = [abs(i-mean) for i in a]

temp = 101
ans = -1

for i in range(n):
    if temp > a[i]:
        temp = a[i]
        ans = i

print(ans)