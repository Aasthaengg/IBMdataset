import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W, A, B = lr()
list1 = '0' * (W-A) + '1' * A
for i in range(H-B):
    print(list1)

list2 = '1' * (W-A) + '0' * A
for i in range(B):
    print(list2)

# 40