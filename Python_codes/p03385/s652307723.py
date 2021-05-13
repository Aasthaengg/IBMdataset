s = input()
ca, cb, cc = 0, 0, 0
for i in range(3):
    if s[i] == 'a':
        ca += 1
    elif s[i] == 'b':
        cb += 1
    else:
        cc += 1

if ca == 1 and cb == 1 and cc == 1:
    print("Yes")
else:
    print("No")