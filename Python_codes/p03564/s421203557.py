n = int(input())
k = int(input())

def defs(n, k):
    seq = 1
    for i in range(n):
        ar = seq * 2
        br = seq + k
        seq = min(ar, br)
    return seq

print(defs(n, k))
