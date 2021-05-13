abc = "abcdefghijklmnopqrstuvwxyz"
a = input()
for i in range(len(abc)):
    if abc[i] not in a:
        print(abc[i])
        exit()
print("None")