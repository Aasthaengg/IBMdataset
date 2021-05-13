S = input()
curr = ""
last = ""
cnt = 0
for c in S:
    curr += c
    if curr != last:
        last = curr
        curr = ""
        cnt += 1
print(cnt)
