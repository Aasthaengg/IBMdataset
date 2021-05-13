S = input()
T = input()

for i in range(len(S)):
    T = T[1:] + T[0]
    if T == S:
        print("Yes")
        break

else:
    print("No")
