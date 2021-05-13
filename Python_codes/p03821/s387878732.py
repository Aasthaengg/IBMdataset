n = int(input())

def comeon():
    for _ in range(n):
        a, b = map(int, input().split())
        yield a, b

ab = list(comeon())

ans = 0
for a, b in ab[::-1]:
    a += ans
    diff = b - a % b if a % b > 0 else 0
    ans += diff

print(ans)