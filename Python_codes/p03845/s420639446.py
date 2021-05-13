from sys import stdin

n = int(input())
t = list(map(int, input().split()))
m = int(input())

sum_t = sum(t)

ans = []
for _ in range(m):
    p, x = map(int, stdin.readline().strip().split())
    ans.append(sum_t - t[p-1] + x)

for i in ans:
    print(i)