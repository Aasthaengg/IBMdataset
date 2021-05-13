import sys


fin = sys.stdin.readline
N = int(fin())
A_list = tuple(int(elem) for elem in fin().split())
num_valid_intervals = 0
# [l, r) is the considered interval
r = 0
cur_sum = 0
cur_xor = 0
for l in range(N):
    item_left = A_list[l]
    while r < N and cur_sum + A_list[r] == cur_xor ^ A_list[r]:
        cur_sum += A_list[r]
        cur_xor ^= A_list[r]
        r += 1
    num_valid_intervals += r - l
    cur_sum -= item_left
    cur_xor ^= item_left
print(num_valid_intervals)
