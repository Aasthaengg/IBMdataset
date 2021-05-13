n, a, b, c, d = list(map(int, input().split()))
s = input()

last = "."
for i in range(a, max(c, d)):
    if last == "#" and s[i] == "#":
        print("No")
        exit()
    last = s[i]

if c < d:
    print("Yes")
else:
    length = 0
    for i in range(b-2, d+1):
        if s[i] == ".":
            length += 1

            if length == 3:
                print("Yes")
                exit()
        else:
            length = 0

    print("No")