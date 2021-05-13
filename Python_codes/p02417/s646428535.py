table = "abcdefghijklmnopqrstuvwxyz"
array = ''
while True:
    try:
        array += str(input().lower())
    except EOFError:
        break

for i in table:
    print(i + " : " + str(array.count(i)))