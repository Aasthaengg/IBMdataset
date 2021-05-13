N=input()
s=N[0]
cnt=1
for i in range(1,4):
    if s==N[i]:
        cnt+=1
        if cnt==3:
            print("Yes")
            exit()
    else:
        cnt=1
        s=N[i]
print("No")