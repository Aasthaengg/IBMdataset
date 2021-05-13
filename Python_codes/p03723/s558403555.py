*l, = map(int, input().split())

ans = 0
while True:
    if l[0]%2 or l[1]%2 or l[2]%2:
        break
    a = (l[1] + l[2]) // 2
    b = (l[0] + l[2]) // 2
    c = (l[0] + l[1]) // 2
    if l == [a, b, c]:
        ans = -1
        break
    l = [a, b, c]
    ans += 1

print(ans)