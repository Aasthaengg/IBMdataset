n, k = [int(x) for x in input().split()]
l_list = sorted([int(x) for x in input().split()], reverse=True)
print(sum(l_list[:k]))