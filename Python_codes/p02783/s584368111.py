ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

H, A = rii()

print((H + A - 1) // A)