s = input()

l = 0
r = len(s)-1
cnt = 0

while l < r:
    lx = 0
    while s[l] == "x" and l < len(s)-1:
        lx += 1
        l += 1

    rx = 0
    while s[r] == "x" and r > 0:
        rx += 1
        r -= 1

    if s[l] == s[r]:
        cnt += abs(rx-lx)

        l += 1
        r -= 1
    else:
        cnt = -1
        break

print(cnt)