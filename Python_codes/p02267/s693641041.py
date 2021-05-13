# encoding: utf-8


class Solution:
    @staticmethod
    def linear_search():
        array_length_1 = int(input())
        array_1 = [int(x) for x in input().split()]
        array_length_2 = int(input())
        array_2 = [int(x) for x in input().split()]

        print(len(list(set(array_1).intersection(set(array_2)))))


if __name__ == '__main__':
    solution = Solution()
    solution.linear_search()