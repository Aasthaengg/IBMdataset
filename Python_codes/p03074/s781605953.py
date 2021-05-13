#!/usr/bin/env python3
# input
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n, k = map(int, input().split())
s = input()
range_len = 2 * k + 1
ans = 0
block_len = []
block_len.append(0)
now = "1"
for i in s:
    if now == i:
        block_len[-1] += 1
    else:
        block_len.append(1)
        now = i
if now == "0":
    block_len.append(0)
l_block = len(block_len)
# print(block_len)
if l_block <= range_len:
    print(n)
else:
    # 尺取
    tmp = sum(block_len[:range_len])
    ans = tmp
    for idx in range(l_block - range_len):
        tmp += block_len[idx + range_len] - block_len[idx]
        # print(tmp, idx)
        if idx % 2 == 1:
            # print(ans, tmp)
            ans = max(ans, tmp)

    print(ans)

