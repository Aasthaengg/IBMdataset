S = input()
cnt = 0
for s in S:
    if s == "x":
        cnt += 1
    if cnt >= 8:
        print("NO")
        exit()
print("YES")