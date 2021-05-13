from sys import stdin

caseIndex = 1
while True:
    x = int(stdin.readline().rstrip())
    if x != 0:
        print("Case %d: %d" % (caseIndex, x))
        caseIndex = caseIndex+1
    else:
        break;
