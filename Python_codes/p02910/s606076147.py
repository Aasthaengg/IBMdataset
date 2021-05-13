a = ["R","U","D"]
b = ["L","U","D"]
s = input()
cnt = 0
for i in range(len(s)):
    if i%2==0:
        if s[i] in a:
            pass
        else:
            cnt = 1
            break
    else:
        if s[i] in b:
            pass
        else:
            cnt = 1
            break
if cnt == 0:
    print("Yes")
else:
    print("No")