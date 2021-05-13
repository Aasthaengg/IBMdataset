S = input()
ans = 0
current = ""
previous = ""
for c in S:
    current += c
    if current != previous:
        previous = current
        current = ""
        ans += 1
print(ans)
