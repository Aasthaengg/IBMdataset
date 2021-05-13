from sys import stdin

s = stdin.readline().rstrip()

print("%s%d%s" % (s[:1], len(s)-2, s[-1]))
