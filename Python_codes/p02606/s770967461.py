from collections import deque
import math

def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

l,r,d = NextInts()

ans = 0
for i in range(l,r+1):
    if i%d == 0:
        ans += 1
print(ans)