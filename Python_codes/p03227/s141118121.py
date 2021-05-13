s = str(input())
if len(s) == 2:
    print(s)
else:
    s = list(s)
    s.reverse()
    print("".join(s))