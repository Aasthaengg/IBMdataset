x, y = list(map(int, input().split()))
g0, g1, g2 = [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2, ]
def num_group(a):
    if a in g0: return 0
    if a in g1: return 1
    if a in g2: return 2
if num_group(x) == num_group(y):
    print('Yes')
else:
    print('No')   