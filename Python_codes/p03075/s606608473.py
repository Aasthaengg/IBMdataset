import itertools


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

# a<b<c<d<e を利用
max_distance = e - a

if max_distance <= k:
    print('Yay!')
else:
    print(':(')

# 全組み合わせの探索
# combs = itertools.combinations([a, b, c, d, e], 2)
# 
# can_connects = [abs(x[0] - x[1]) <= k for x in combs]
# 
# if all(can_connects):
#     print('Yay!')
# else:
#     print(':(')


