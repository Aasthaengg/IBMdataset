def num_divide_two(num: int):
    return int(format(num, 'b')[::-1].find("1"))

N = int(input())
print(sum(map(num_divide_two, map(int, input().split()))))