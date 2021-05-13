n = int(input())
p = [int(i) for i in input().split()]
'''
i == x となる点で、i+1とスワップする
境界に注意
'''
ans = 0
for i in range(n):
    if i < n-1 and p[i] == i+1:
        p[i+1] = p[i]
        ans += 1
    elif i == n-1 and p[i] == i+1:
        ans += 1
print(ans)