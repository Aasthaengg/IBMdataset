N = int(input())
List = list(map(str, input().split()))
import collections
c = collections.Counter(List)
#print(c)
if len(c)==N:
    print('YES')
else:
    print('NO')