s = input()
t = input()


u = s + s

flag = False
j = 0

for i in range(len(u)):
    if u[i] == t[j]:
        j += 1
        if j == len(t):
            flag = True
            break
    else:
        j = 0

if flag:
    print("Yes")
else:
    print("No")