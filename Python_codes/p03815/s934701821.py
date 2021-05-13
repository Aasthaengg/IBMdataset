x = int(input())
loopn = (x//11) * 2
rm = x % 11
if rm == 0:
    pass
elif rm <= 6:
    loopn += 1
else:
    loopn += 2
print(loopn)