s = input()
k = True

for i in range(1, len(s)+1):
    if i % 2 == 1:
        if s[i-1] == 'R' or s[i-1] == 'U' or s[i-1] == 'D':
            pass
        else:
            k = False
            break
    elif i % 2 == 0:
        if s[i-1] == 'L' or s[i-1] == 'U' or s[i-1] == 'D':
            pass
        else:
            k = False
            break

if k == True:
    print("Yes")
elif k == False:
    print("No")
