S = input()
T = input()
for i in range(len(S)):
    if T == S:
        print("Yes")
        exit()
    else:
        T = T[-1] + T[:-1]
print("No")
