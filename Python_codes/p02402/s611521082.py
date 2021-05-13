n = input()
a = map(int, raw_input().split())
if len(a) == n:
    print "%d %d %d" % (min(a), max(a), sum(a))