# encoding: utf-8

import sys
from collections import deque


class Solution:
    @staticmethod
    def message_queue():
        # write your code here
        # array_length = int(input())
        _input = sys.stdin.readlines()
        task_num = int(_input[0].split()[0])
        task_time = int(_input[0].split()[1])
        total_time = 0

        task_deque = deque([{'name': i.split()[0], 'time': int(i.split()[1])} for i in _input[1:]])

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