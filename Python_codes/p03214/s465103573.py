import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

mean = sum(a) / n

ans = [200, 200]

for i in range(n):
    if abs(mean - a[i]) < ans[1]:
        ans = [i, abs(mean - a[i])]

print(ans[0])
