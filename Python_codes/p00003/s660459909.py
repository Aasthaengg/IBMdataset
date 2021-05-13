n = int(raw_input())
for i in range(n):
    e = map(int, raw_input().split())
    e.sort()
    if e[2] * e[2]== e[0] * e[0] + e[1] * e[1]:
        print "YES"
    else:
        print "NO"