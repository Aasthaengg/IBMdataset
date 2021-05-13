def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, B, C = MI()

print(max(C - A + B, 0))