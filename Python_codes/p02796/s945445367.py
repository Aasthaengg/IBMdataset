n = int(input())
rom = []
for _ in range(n):
    x, l = map(int, input().split())
    rom.append([x + l, x - l])
    
rom.sort()
ans = 0
pos = -10 ** 10
for end, start in rom:
    if start >= pos:
        ans += 1
        pos = end
print(ans)