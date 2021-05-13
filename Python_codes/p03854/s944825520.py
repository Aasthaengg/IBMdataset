S = input()

while 1:

    flag = 0
    if S[-5:] == "erase":
        S = S[:-5]
        flag = 1
    if S[-6:] == "eraser":
        S = S[:-6]
        flag = 1
    if S[-5:] == "dream":
        S = S[:-5]
        flag = 1
    if S[-7:] == "dreamer":
        S = S[:-7]
        flag = 1

    if flag == 0:
        break

if S=="":
    print("YES")
else:
    print("NO")
