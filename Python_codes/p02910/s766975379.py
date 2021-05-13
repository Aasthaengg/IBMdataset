s = input()

for i in range(len(s)) :
    if i % 2 != 0 :
        if s[i] != "L" and s[i] != "U" :
            if s[i] != "D" :
                print("No")
                break
    elif i % 2 == 0 :
        if s[i] != "R" and s[i] != "U" :
            if  s[i] != "D" :
                print("No")
                break

else :
    print("Yes")
