t=input()
ans = ""
for i in range(len(t)):
    if (i % 2 == 1) and (t[i] == "R"):
        ans = "No"
        break
    elif (i % 2 == 0) and (t[i] == "L"):
        ans = "No"
        break

if ans == "No":
    print("No")
else:
    print("Yes")
