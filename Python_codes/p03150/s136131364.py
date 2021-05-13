from sys import stdin
from sys import setrecursionlimit
import bisect
setrecursionlimit(10 ** 7)

s = input()
point = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        now = s[:i]+s[j:]
        if now == "keyence":
            print("YES")
            exit()
print("NO")