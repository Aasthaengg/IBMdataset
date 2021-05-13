s = raw_input()
n = input()
result = []
for i in xrange(n):
    c = raw_input().split()
    a = int(c[1])
    b = int(c[2])+1

    if c[0] == 'print' :
        result.append(s[a:b])
    elif c[0] == 'reverse':
        d = s[a:b]
        s = s.replace(d,d[::-1])
    elif c[0] == 'replace':
        s = s[:a] + c[3] + s[b:]

for i in result:
    print i