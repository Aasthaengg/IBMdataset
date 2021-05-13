def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B = MI()

print((-1) ** int(B % A != 0) * A + B)