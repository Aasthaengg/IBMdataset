s = input()
prev = None
total = 0
for i in s:
    if prev == None:
        prev = i
    else:
        if (i != prev):
            total += 1
            prev = i
        else:
            pass
print(total)