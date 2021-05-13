# 131 A

s = input()
cnd = True

for i in range(0, len(s)-1):
    # print(i)
    if int(s[i]) == int(s[i+1]):
        cnd = False
        break

if cnd == True:
    print("Good")
else:
    print("Bad")