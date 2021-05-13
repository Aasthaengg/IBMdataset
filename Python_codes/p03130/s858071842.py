town = [0] * 4
for _ in range(3):
    a, b = map(int, input().split())
    town[a-1] += 1
    town[b-1] += 1
if 3 in town or 4 in town:
    ans = 'NO'
else:
    ans = 'YES'
print(ans)
