N = int(input())
A = sorted(list(map(int, input().split())))
offset = True if len(A) % 2 == 0 else False
alice = sum(A[offset::2])
bob = sum(A[not offset::2])
print(alice-bob)
