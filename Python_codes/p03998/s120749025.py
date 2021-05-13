import sys


def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


def input():
    return sys.stdin.readline().rstrip()


#############
# Main Code #
#############
sa = list(input())
sb = list(input())
sc = list(input())

s = [sa, sb, sc]
now = s[0].pop(0)

while True:
    if not len(s[ord(now) - 97]):
        break

    now = s[ord(now) - 97].pop(0)

if now == 'a':
    print('A')
elif now == 'b':
    print('B')
else:
    print('C')
