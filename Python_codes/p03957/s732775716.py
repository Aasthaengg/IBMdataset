s = input()
flg = 0
for i in range(len(s)):
    if s[i] == "C":
        for j in range(i,len(s)):
            if s[j] == "F":
                flg = 1
if flg == 1:
    print("Yes")
else:
    print("No")   