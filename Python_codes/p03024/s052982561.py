S = input()
win = S.count('o')
lose = S.count('x')
remain = 15 - len(S)
if remain + win >= 8:
    print("YES")
else:
    print("NO")