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
a = getN()
b = getN()
h = getN()
print(h * (a + b) // 2)
