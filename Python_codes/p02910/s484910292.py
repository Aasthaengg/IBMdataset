# B Tap Dance
s = input()
S = len(s)
for i in range(S):
    if i % 2:  # 奇数
        if s[i] == "R":
            print("No")
            exit()
    else:
        if s[i]  == "L":
            print("No")
            exit()
print("Yes")