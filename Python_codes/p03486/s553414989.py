s = sorted(input())
t = sorted(input())[::-1]
flag = -1
for i,j in zip(s,t):
    if ord(i) < ord(j):
        flag = 1
        break
    elif ord(i) == ord(j):
            flag = 0
    else:
        flag = -1
        break

if flag ==1:
    print("Yes")
elif flag == -1:
    print("No")
else:
    if len(s) < len(t):
        print("Yes")
    elif len(s) >= len(t):
        print("No")