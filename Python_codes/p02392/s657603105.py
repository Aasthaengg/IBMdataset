i = input()
i = i.split(" ")
i = list(map(int,i))

if i[0] < i[1] and i[1] < i[2]:
    print("Yes")
else:
    print("No")