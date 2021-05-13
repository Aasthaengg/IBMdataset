s = input()
now = 100000000000
for i in range(len(s)-2):
    chk = abs(753 - int(s[i:i+3]))
    if i == 0:
        now = chk
    elif chk < now:
        now = chk
print(now)