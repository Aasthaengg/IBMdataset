import collections


s = ''
while True:
    try:
        s += input().lower()
    except EOFError:
        break
c = collections.Counter(s)
for i in range(97, 123):
    print("{} : {}".format(chr(i), c[chr(i)]))

