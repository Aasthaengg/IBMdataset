import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
x_li = [int(w) for w in input().split()]

ans = 0
for x in x_li:
    ans += min(x, abs(k - x))

print(ans*2)
