import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

s1, s2, s3 = input().split()
print(''.join([s1[0], s2[0], s3[0]]).upper())