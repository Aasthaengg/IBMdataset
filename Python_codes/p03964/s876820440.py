#!/usr/bin/env python3
n = int(input())
cur_t = 1
cur_a = 1
for i in range(n):
    t, a = map(int, input().split())
    times = max(-(-cur_t // t), -(-cur_a // a))
    cur_t = t * times
    cur_a = a * times
    # print(cur_t, cur_a)
print(cur_t + cur_a)
