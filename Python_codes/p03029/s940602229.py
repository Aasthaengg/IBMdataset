def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

A, P = MI()

print((3 * A + P) // 2)