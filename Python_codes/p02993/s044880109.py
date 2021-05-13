import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = input()
for i in range(3):
    if S[i]==S[i+1]:
        print('Bad')
        break
else:
    print('Good')