N = int(input())

found = False
for x in range(0, 25+1):
    for y in range(0, 14+1):
        if 4 * x + 7 * y == N:
            found = True
if found:
    print("Yes")
else:
    print("No")
