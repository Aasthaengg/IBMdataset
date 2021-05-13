import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
counter = collections.Counter(A)
total = 0
for k, v in counter.items():
    total += k * v
for i in range(Q):
    B, C = map(int, input().split())
    if counter.get(B) != None:
        count = counter.pop(B)
        counter[C] = counter.get(C, 0) + count
        total -= count * B
        total += count * C
    print(total)
