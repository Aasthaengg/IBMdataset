n = int(input())
data = list(map(int, input().split()))
ans = 0
prev = False
for idx, d in enumerate(data):
    if d == idx + 1 and prev is False:
        ans += 1
        prev = True
    else:
        prev = False
print(ans)