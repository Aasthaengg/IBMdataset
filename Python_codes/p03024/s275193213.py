k = input()
win_count = 0
lose_count = 0
for i in range (len(k)):
    if k[i] == "o":
        win_count += 1
    else:
        lose_count += 1
if win_count + (15-len(k))>= 8:
    print("YES")
else:
    print("NO")
