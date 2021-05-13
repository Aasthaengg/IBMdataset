S = input()

listed = list(S)

if len(listed) == 2:
    print(listed[0] + listed[1])
elif len(listed) == 3:
    print(listed[2] + listed[1] + listed[0])