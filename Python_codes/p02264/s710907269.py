# encoding: utf-8

import sys
from collections import deque

input_ = sys.stdin.readlines()


def message_queue():
    # write your code here
    n, shard = map(int, input_[0].split())

    task_deque = deque(map(lambda x: x.split(), input_[1:]))
    t_accu = 0

    while task_deque:
        t_name, t_time = task_deque.popleft()
        t_time = int(t_time)
        if t_time <= shard:
            t_accu += t_time
            print(t_name, t_accu)
        else:
            t_time -= shard
            t_accu += shard
            task_deque.append([t_name, t_time])


message_queue()