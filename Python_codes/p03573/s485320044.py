nums = list(map(int,input().split()))
import collections
c = collections.Counter(nums)

print(c.most_common()[1][0])