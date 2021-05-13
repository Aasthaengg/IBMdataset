ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

N = int(input())
A = [v for v in rii() if v % 2 == 0]

print("APPROVED" if all(v % 3 == 0 or v % 5 == 0 for v in A) else "DENIED")