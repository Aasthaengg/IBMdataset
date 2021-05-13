import sys
input = sys.stdin.readline

p = [int(x) for x in input().split()] 
print(sum(p) - max(p))

