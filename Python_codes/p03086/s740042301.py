S = input()

ans = 0
j = 0
for i in S:
    if i == "A" or i == "C" or i == "G" or i == "T":
        j += 1
        if ans < j:
            ans = j
    else:
        j = 0

print(ans)