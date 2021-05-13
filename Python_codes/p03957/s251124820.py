s = input()
if "C" in s and "F" in s:
    for i in range(len(s)):
        if s[i]=="C":
            ind = i
            break
    flag = 0
    for j in range(ind,len(s)):
        if s[j]=="F":
            flag = 1
            break
    if flag==1:
        print("Yes")
    else:
        print("No")
else:
    print("No")