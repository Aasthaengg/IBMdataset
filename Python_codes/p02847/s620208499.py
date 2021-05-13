from sys import stdin
from sys import setrecursionlimit
import bisect
setrecursionlimit(10 ** 7)

s = input()

li = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

print(7-li.index(s))