N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    s = 0
    for j in range(len(str(i))):
        s += int(str(i)[j])
    if A <= s <= B:
        ans += i
print(ans)
