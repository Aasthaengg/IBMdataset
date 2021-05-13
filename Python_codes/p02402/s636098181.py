n=int(raw_input())
num_list = [int(x) for x in raw_input().split(" ")][:n]
print "%d %d %d" % (min(num_list), max(num_list), sum(num_list))