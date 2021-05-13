import sys
sys.setrecursionlimit(10 ** 7)

x,y = map(int,input().split())
ans = 0

for i in range(10**7):
    if x > y:
        break
    ans += 1
    x = 2 * x

print(ans)