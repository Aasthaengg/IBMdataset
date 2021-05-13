S = input()

flag = 0

words = ("dream","erase","dreamer","eraser")
count = 0

while len(S) >= 5:

    for i in words:
        N = len(i)
        if S[-N:] in words:
            n = len(S) - N
            S = S[:n]
            flag = 1
            break
        else:
            flag = 0
            continue


    if flag == 0:
        break



if len(S) == 0:
    print("YES")
else:
    print("NO")