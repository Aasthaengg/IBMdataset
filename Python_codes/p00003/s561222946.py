n = input()

for i in range(n):
    l = map(int, raw_input().strip().split(" "));
    l.sort();
    if (l[2] ** 2 == l[1] ** 2 + l[0] ** 2):
        print "YES"
    else:
        print "NO"