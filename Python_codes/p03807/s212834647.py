import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = map(int, input().split())

odd = 0

for i in a:
    if i % 2 == 1:
        odd += 1

ans = "YES" if odd % 2 == 0 else "NO"

print(ans)
