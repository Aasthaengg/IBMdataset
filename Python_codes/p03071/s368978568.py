def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B = MI()

print(max(2 * A - 1, A + B, 2 * B - 1))