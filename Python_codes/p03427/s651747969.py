import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = [int(i) for i in list(input())]
length = len(N)

for l in N[1:]:
    if not l==9:
        ans = (length-1)*9+(N[0]-1)
        print(ans)
        break
else:
    print(sum(N))
