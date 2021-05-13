s=input()
b=False
for i in s:
    if i=="C":
        b=True
    if b and i=="F":
        print("Yes")
        exit()
print("No")