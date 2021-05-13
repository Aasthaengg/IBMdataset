n = int(input())

c = list(input())
cnt = 0
l = 0
r = n-1
while l < r:
    while c[l] == "R" and l < r:
        l += 1

    while c[r] == "W" and l < r:
        r -= 1

    if c[l] == c[r]:
        break

    c[l], c[r] = c[r], c[l]

    l += 1
    r -= 1
    cnt += 1

print(cnt)