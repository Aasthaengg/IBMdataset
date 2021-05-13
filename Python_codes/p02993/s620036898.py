s = input()

flg = True
for a, b in zip(s, s[1:]):
    if a == b:
        flg = False
print("Good" if flg else"Bad")
