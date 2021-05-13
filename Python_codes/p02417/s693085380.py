import sys
hoge = { chr(x):0 for x in range(ord('a'), ord('z')+1)}
a = list()
for line in sys.stdin:
    a.append(line)
for line in a:
    for x in line:
        if x.lower() not in hoge:
            continue
        else:
            hoge[x.lower()] += 1
for k, v in sorted(hoge.items()):
    print ('{} : {}'.format(k, v))
