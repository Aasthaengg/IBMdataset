n, a, b, c, d = map(int, input().split())
s = str(input())
a -= 1
b -= 1
c -= 1
d -= 1



if c < d:
    for i in range(b, d):
        if s[i:i+2] == "##":
            print("No")
            exit()
    for i in range(a, c):
        if s[i:i+2] == "##":
            print("No")
            exit()
    print("Yes")

elif c == d:
    print("No")

else:
    for i in range(b, d):
        if s[i:i + 2] == "##":
            print("No")
            exit()
    for i in range(a, c):
        if s[i:i + 2] == "##":
            print("No")
            exit()
    for i in range(b-1, d):
        if s[i:i+3] == "...":
            print("Yes")
            exit()
    print("No")