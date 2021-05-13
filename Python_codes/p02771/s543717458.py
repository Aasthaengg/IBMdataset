ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

A, B, C = rii()

print("Yes" if len(set([A, B, C])) == 2 else "No")