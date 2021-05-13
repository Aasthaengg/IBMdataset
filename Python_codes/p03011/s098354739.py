def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

P, Q, R = MI()

print(P + Q + R - max(P, Q, R))