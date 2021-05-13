import sys
input = sys.stdin.readline

N = int(input())
b = 7 + 10**9
ans = 1
for i in range(1, N + 1):
    ans = i * (ans % b)
print(ans % b)
