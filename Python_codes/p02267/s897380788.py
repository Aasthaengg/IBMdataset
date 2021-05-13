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
        length_1 = int(self.__input[0])
        array_1 = list(map(int, self.__input[1].split()))
        length_2 = int(self.__input[2])
        array_2 = list(map(int, self.__input[3].split()))

        assert length_1 == len(array_1) and length_2 == len(array_2)

        count = 0
        for each in array_2:
            if self.linear_search(key=each, array=array_1, array_length=length_1):
                count += 1

        return str(count)

    @staticmethod
    def linear_search(key, array, array_length):
        # print(len(set(array_1).intersection(set(array_2))))
        for i in range(array_length):
            if array[i] == key:
                return True
        return False


if __name__ == '__main__':
    case = Solution()
    print(case.solution)