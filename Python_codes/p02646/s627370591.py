a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

ans = False

if v > w:
    diff = abs(a - b)
    ans = diff / (v - w) <= t

print("YES" if ans else "NO")