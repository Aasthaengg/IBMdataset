S = input()

ans = 0
count = 0
flag = False
for s in S:
    if flag:
        count += 1
        if s == "Z":
            ans = count
    else:
        if s == "A":
            flag = True
            count += 1

print(ans)