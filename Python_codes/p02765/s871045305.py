ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

N, R = rii()

if N > 10:
    print(R)
else:
    print(R + (100*(10-N)))