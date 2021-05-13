n = int(input())
c = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x == y:c += 1
    else: c = 0
    if c == 3: break
print('No' if c < 3 else 'Yes')
