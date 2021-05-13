import sys
input()
mx = -float('inf')
res = mx
mn = int(input())
for i in map(int,sys.stdin.readlines()):
        if mx < i - mn:
            mx = i - mn
        if 0 > i - mn:
            mn = i
        res = max(mx,res)
print(res)