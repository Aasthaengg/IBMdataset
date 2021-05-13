def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B = MI()

if A <= 5:
    print(0)
elif A >= 13:
    print(B)
else:
    print(B // 2)