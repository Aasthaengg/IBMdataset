import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
from collections import defaultdict
dic = defaultdict(int)

for _ in range(N):
    s = list(input())
    s.sort()
    dic[''.join(s)] += 1

ans = 0
for n in dic.keys():
    ans += dic[n]*(dic[n]-1)//2

print(ans)