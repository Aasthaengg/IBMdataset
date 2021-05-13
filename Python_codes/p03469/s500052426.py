import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

S = list(input())
S[3] = '8'

print (''.join(S))