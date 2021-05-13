S = input()

flug = True
for i, value in enumerate(S):
    if i % 2 == 0:
        if value == 'L':
            flug = False
    else:
        if value == 'R':
            flug = False
if flug:
    print("Yes")
else:
    print("No")