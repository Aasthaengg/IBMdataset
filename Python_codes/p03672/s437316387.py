s = input()
if len(s) % 2 == 1:
    s = s[:-1]
else:
    s = s[:-2]
while True:
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        exit()
    else:
        s = s[:-2]