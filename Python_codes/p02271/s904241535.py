a={0}
input()
for c in raw_input().split():
    for i in a.copy(): a.add(i+int(c))
input()
for c in raw_input().split():
    print "yes" if int(c) in a else "no"