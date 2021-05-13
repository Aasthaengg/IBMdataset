n, a, b, c, d = map(int, input().split())
s = list(input())
jud = True

for i in range(min(a, b) - 1, max(c, d) - 1):
    if s[i] == "#":
        if s[i + 1] == "#":
            jud = False
            break

if (a < b and c > d and jud) or (a > b and c < d and jud):
    jud = False
    for i in range(max(a, b) - 2, min(c, d) - 1):
        if s[i] == ".":
            if s[i + 1] == "." and s[i + 2] == ".":
                jud = True

if jud:
    print("Yes")
else:
    print(("No"))