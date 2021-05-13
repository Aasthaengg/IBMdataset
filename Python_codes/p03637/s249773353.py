n = int(input())
a = [int(x) for x in input().split()]
four = 0
two = 0
el = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0 :
        two += 1
    else:
        el += 1

if two == 0:
    if four + 1 >= el:
        print("Yes")
    else:
        print("No")
else:
    if four >= el:
        print("Yes")
    else:
        print("No")
