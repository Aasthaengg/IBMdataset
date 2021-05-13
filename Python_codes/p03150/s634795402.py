S = input().strip()
if S=="keyence":
    print("YES")
else:
    flag = 0
    for i in range(len(S)):
        for j in range(i,len(S)):
            x = S[:i]+S[j+1:]
            if x=="keyence":
                flag = 1
                break
        if flag==1:break
    if flag==1:
        print("YES")
    else:
        print("NO")