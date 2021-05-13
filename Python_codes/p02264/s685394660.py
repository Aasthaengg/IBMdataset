# encoding: utf-8

import sys
from collections import deque


class Solution:
    @staticmethod
    def message_queue():
        # write your code here
        # tasks = deque(map(lambda x: x.split(), sys.stdin.readlines()))
        task_num, task_time = map(int, input().split())
        _input = sys.stdin.readlines()
        
        task_deque = deque(map(lambda x: dict(name=x.split()[0], time=int(x.split()[-1])), _input))
        total_time = 0

        while task_deque:
            item = task_deque.popleft()
            if item['time'] <= task_time:
                total_time += item['time']
                print(item['name'], total_time)
            else:
                item['time'] -= task_time
                total_time += task_time
                task_deque.append(item)


if __name__ == '__main__':
    solution = Solution()
    solution.message_queue()