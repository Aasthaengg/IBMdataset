# abc103
S = input()
T = input()
temp = S
for i in range(len(S)):
    if temp == T:
        print("Yes")
        exit()
    else:
        temp = temp[-1] + temp[:-1]
print("No")
