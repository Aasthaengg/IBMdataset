s = input()
s_origin = s
n = len(s)

for i in range(n):
    for j in range(ord("a"), ord("z")+1):
        if not (chr(j) in s) and \
            s + chr(j) != s_origin and \
                s_origin < s + chr(j):
            print(s + chr(j))
            exit()
    if len(s) == 1 and s != "z":
        print(chr(ord(s) + 1))
        exit()
    s = s[:-1]

print(-1)