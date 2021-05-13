import string
data = {}
while True:
    try:
        in_str = raw_input()
        for c in in_str:
            if c.isalpha() == False or c.lower() < 'a' and 'z' < c.lower():
                continue
            if c.lower() in data:
                data[c.lower()] += 1
            else:
                data[c.lower()] = 1
    except(EOFError):
        break
for c in string.lowercase[:26]:
    if c in data:
        print c + ' : ' + str(data[c])
    else:
        print c + ' : 0'