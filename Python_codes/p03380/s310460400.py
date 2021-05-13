n = int(input())
a_list = list(map(int,input().split()))
a_list.sort()
a_max = a_list.pop()
result = []
import math
for a in a_list:
  result.append(abs(math.ceil(a_max /2) - a))

print(a_max,a_list[result.index(min(result))])
