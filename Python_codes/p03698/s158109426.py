s = input()
flag = 1
for i in range(len(s)-1) :
    for j in range(i+1,len(s)) :
        if s[i] == s[j] :
            flag = 0

if flag == 1 :
    print("yes")
else :
    print("no")
