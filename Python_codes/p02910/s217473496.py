S = input()
flag = 0
for i in range(1,len(S)+1):
    if i%2 == 1:
        if S[i-1] in 'RUD':
            continue
        else:
            flag =1
            print("No")
            break
    else:
        if S[i-1] in 'LUD':
            continue
        else:
            flag = 1
            print("No")
            break
if flag == 0:
    print("Yes")