s = input()
t = input()

flag = 0

if(len(t)> len(s)):
    print("UNRESTORABLE")
else:
    for i in reversed(range(len(s)-len(t)+1)):
        for j in range(len(t)):
            if(s[i+j] == t[j] or s[i+j] == "?"):
                if(j == len(t) -1):
                    flag = 1
                    break
            else:
                break

        if(flag == 1):
            break

    if(flag == 0):
        print("UNRESTORABLE")
    else:
        kotae = list(s[0:i] + t + s[i+len(t):])
        for i in range(len(kotae)):
            if(kotae[i] == "?"):
                kotae[i] = "a"
        kotae = "".join(kotae)
        print(kotae)