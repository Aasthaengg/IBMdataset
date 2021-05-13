###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

S = input()
w = int(input())

print(S[::w])


