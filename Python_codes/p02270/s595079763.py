# encoding: utf-8


import sys


class Solution:
    def __init__(self):
        """
        init input array
        """
        self.__input = sys.stdin.readlines()

    @property
    def solution(self):
        product_num = int(self.__input[0].split()[0])
        truck_num = int(self.__input[0].split()[1])
        weight_list = list(map(int, self.__input[1:]))

        assert product_num == len(weight_list)

        # binary search
        left, right, mid = max(weight_list), sum(weight_list), 0
        while left < right:
            mid = (left + right) // 2
            # check return True : p could be smaller
            if self.check(mid, weight_list, truck_num):
                right = mid
            else:
                mid += 1
                left = mid
        return str(mid)

    @staticmethod
    def check(max_load_cursor, weight_list, truck_num):
        track_count = 1
        current_load = 0
        for item_weight in weight_list:
            current_load += item_weight
            # change to next truck
            if current_load > max_load_cursor:
                current_load = item_weight
                track_count += 1
                if track_count > truck_num:
                    return False
        return True


if __name__ == '__main__':
    case = Solution()
    print(case.solution)