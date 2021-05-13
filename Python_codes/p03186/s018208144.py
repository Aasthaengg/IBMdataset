import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,c = map(int, input().split())

ans = min(c,(a+b+1))
ans += b
print(ans)