s = input()
al = [chr(i) for i in range(97, 97+26)]
l = list(s)
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(s) == 26:
    for i in range(24, -1, -1):
        for j in range(25, i, -1):
            if s[i] < s[j]:
                print(s[:i] + s[j])
                exit()
else:
    for i in al:
        if not i in s:
            print(s + i)
            exit()