n, a, b, c, d = map(int, input().split())
s = input()
if "##" in s[a - 1:max(c, d)]:
    print("No")
    exit()
elif c > d and not "..." in s[b - 2:d + 1]:
    print("No")
    exit()
print("Yes")