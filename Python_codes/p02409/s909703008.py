n = input()
floor = []
for i in range(n):
    floor.append(map(int,raw_input().split()))

bill = [ [ [ 0 for c in range(10)] for b in range(3)] for a in range(4)]

for a in floor:
    bill[a[0]-1][a[1]-1][a[2]-1] = (bill[a[0]-1][a[1]-1][a[2]-1]) + (a[3])
flg = 0
for a in bill:
    if flg == 1:
        print "####################"
    for b in a:
        print " " + " ".join(map(str,b))
        flg = 1