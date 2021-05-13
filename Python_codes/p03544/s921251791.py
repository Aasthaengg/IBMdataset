import copy

n = int(input())
if n == 1:
    print(1)
    exit()

l_2 = 0
l_1 = 2
l_0 = 1
for i in range(2, n+1):
    l_2 = copy.deepcopy(l_1)
    l_1 = copy.deepcopy(l_0)
    l_0 = l_1 + l_2
print(l_0)