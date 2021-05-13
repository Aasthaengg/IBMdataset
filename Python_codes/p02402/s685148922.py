if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(min(nums), max(nums), sum(nums))