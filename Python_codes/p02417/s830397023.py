from collections import OrderedDict

d = OrderedDict((chr(i), 0) for i in range(ord('a'), ord('a')+26))

while True:
    try:
        s = input()
    except EOFError:
        break
    else:
        for c in s.lower():
            if c in d:
                d[c] += 1

for k, v in d.items():
    print("{} : {}".format(k, v))