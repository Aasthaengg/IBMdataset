s = input()
t = input()

cont = 0

if len(s)+1 == len(t):
    for i in range(len(s)):
        if s[i] == t[i]:
            cont += 1
    if cont == len(s):
        print("Yes")
    else:
        print("No")
else:
    print("No")
