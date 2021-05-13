a = [chr(i) for i in range(97, 123)]
line = ''
while True:
    try:
        line += input().lower()
    except:
        break
for c in a:
    print("{0} : {1}".format(c, line.count(c)))