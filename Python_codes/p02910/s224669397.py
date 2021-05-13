S = input()
N = len(S)
for i in range(N):
    if i%2==0:
        if not(S[i]=="R" or S[i]=="U" or S[i]=="D"):
            print("No")
            break

    else:
        if not (S[i]=="L" or S[i]=="U" or S[i]=="D"):
            print("No")
            break
else:
    print("Yes")