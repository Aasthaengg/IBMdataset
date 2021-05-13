def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]

s = inp()

if s == "RRR":
    print(3)
elif s == "SSS":
    print(0)
elif s == "RSS" or s == "SSR" or s == "RSR" or s == "SRS":
    print(1)
else:
    print(2)