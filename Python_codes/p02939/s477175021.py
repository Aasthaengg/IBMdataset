S = input()

ans = 0
prev = ''
curr = ''
for s in S:
    curr += s
    if prev != curr:
        ans += 1
        prev = curr
        curr = ''
print(ans)
