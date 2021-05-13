n = int(input())
in_list = [int(s) for s in input().split()]
print("%d %d %d" % (min(in_list), max(in_list), sum(in_list)))