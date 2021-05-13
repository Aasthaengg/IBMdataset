n = int(input())

i = n
while True:
    if str(i)[0] != str(i)[1] or str(i)[1] != str(i)[2]:
        i += 1
    else:
        break
print(i)
