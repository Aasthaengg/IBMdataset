import math
tree_num, range = map(int,input().split())

range_num = range * 2 + 1

print(math.ceil(tree_num / range_num))
