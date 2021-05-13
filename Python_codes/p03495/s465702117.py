import collections
n,k = map(int,input().split())
a = list(map(int,input().split()))

a_cnt = collections.Counter(a)
#print(a_cnt)
a_sort = sorted(a_cnt.values(),reverse=True)
#print(a_sort)
#print(a_sort[k:])
print(sum(a_sort[k:]))
