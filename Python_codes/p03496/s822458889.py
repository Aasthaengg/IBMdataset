def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

n = getN()
nums = getlist()
ln = len(nums)
maxn, minn = max(nums), min(nums)
already = False

if minn >= 0:
    plus = True

if maxn < 0:
    plus = False

if maxn >= 0 and minn < 0:
    print(ln*2-1)
    already = True
    if abs(maxn) > abs(minn):
        source = nums.index(maxn)
        plus = True
    else:
        source = nums.index(minn)
        plus = False
    for i in range(len(nums)):
        print(source+1, i+1)

if not already:
    print(ln-1)

if plus:
    for i in range(ln-1):
        print(i+1, i+2)
else:
    for i in range(ln-1):
        print(ln-i, ln-i-1)






