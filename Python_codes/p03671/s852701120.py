import sys
input = sys.stdin.readline
li = [int(i) for i in input().split()]
li.sort()
print(li[0] + li[1])