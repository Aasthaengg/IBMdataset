S=input()
ans = 0
prev = ''
temp = ''
for c in S:
    temp += c
    if temp != prev:
        ans += 1
        prev = temp
        temp = ''

print(ans)
