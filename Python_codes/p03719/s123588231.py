###template###
import sys
input = sys.stdin.readline
def mi(): return map(int, input().split())
###template###

A, B, C = mi()

if C >= A and C <= B:
    print('Yes')
    exit()
print('No')


