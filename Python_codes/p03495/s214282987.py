import collections
n, k = map(int, input().split())
list = input().split()
c_list = collections.Counter(list)
sorted_c_list = sorted(c_list.values(),reverse=True)
print(sum(sorted_c_list[k:]))