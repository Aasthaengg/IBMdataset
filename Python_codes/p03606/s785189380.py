from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())

ans = 0

for _ in range(n):
    i, j = map(int, input().split())
    ans += j - i + 1

print(ans)