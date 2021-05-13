S = input()

cf = "CF"
i = 0
for s in S:
    if s == cf[i]:
        i += 1

    if i == 2:
        break

if i == 2:
    print("Yes")
else:
    print("No")
