import math
import itertools

N = int(input())
A = list(map(int, input().split()))
ans = []

for i in itertools.combinations(A,2):
    a,b = int(i[0]), int(i[1])
    s = a*b
    ans.append(s)

print(sum(ans))
