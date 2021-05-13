from collections import deque
import math

def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

n = NextInt()
da = NextIntList()
ans = 0
for i in range(n):
    if i%2 == 0 and da[i]%2 == 1:
        ans += 1

print(ans)