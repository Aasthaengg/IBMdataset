a = input()
l = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    if a == l[i]:
        print(l[i+1])
        exit()
