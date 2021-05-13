s = input()
cnt = 0
for i in s:
    if i == "x":
        cnt += 1
if cnt > 7:
    print("NO")
else:
    print("YES")