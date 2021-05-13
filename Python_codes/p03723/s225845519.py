A, B, C = [int(x) for x in input().split()]

def IsOdd(a, b, c):
    if a % 2 == 1:
        return True
    if b % 2 == 1:
        return True
    if c % 2 == 1:
        return True
    return False

def Exchange(a, b, c):
    retA = 0
    retB = 0
    retC = 0
    retA = (b // 2) + (c // 2)
    retB = (a // 2) + (c // 2)
    retC = (a // 2) + (b // 2)
    return retA , retB , retC

cnt = 0
routedA = []
while True :
    if IsOdd(A, B, C):
        break
    if A in routedA:
        cnt = -1
        break
    routedA.append(A)
    cnt += 1
    ret = Exchange(A, B, C)
    A = ret[0]
    B = ret[1]
    C = ret[2]

print(cnt)

