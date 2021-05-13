s = input()
ch = s[-1]
index = len(s) - 1
answ = 0
while index >= 0:
    if s[index] != ch:
        answ += 1
        ch = 'B' if ch == 'W' else 'W'
    else:
        index -= 1
print(answ)
