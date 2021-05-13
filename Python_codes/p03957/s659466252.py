s = input()
res = ""
for letter in s:
    if res == "" and letter =="C":
        res += letter
    elif res =="C" and letter == "F":
        res +=letter
        break
    else:
        continue
if res == "CF":
    print("Yes")
else:
    print("No")
