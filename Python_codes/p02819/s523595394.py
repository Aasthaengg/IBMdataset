import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())
double = X*10+1
s = set()
for i in range(2, double):
    if i in s:
        continue
    if i>=X:
        print(i)
        break
    cnt = 1
    while cnt*i<=double:
        s.add(i*cnt)
        cnt += 1