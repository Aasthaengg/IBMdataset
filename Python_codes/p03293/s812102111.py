s = input()
t = input()

rev_s = ""
flag = 0

for i in range(len(t)):
    t = t[-1] + t[:len(t)-1]
    # print(t)

    if s == t:
        flag  = 1
        break
    else:
        flag  = 0

if flag == 1:
    print("Yes")
else:
    print("No")