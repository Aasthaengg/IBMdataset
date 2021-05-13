target = input()
result = 0
while True:
    sen = input()
    if sen == "END_OF_TEXT": break
    result += [i.lower() for i in sen.split()].count(target)
print(result)
