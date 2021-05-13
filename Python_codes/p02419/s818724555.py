cnt = 0
W = input()
while True:
    li = input().split()
    if li[0] == "END_OF_TEXT":
        break
    for w in li:
        if w.lower() == W:
            cnt += 1
print(cnt)

