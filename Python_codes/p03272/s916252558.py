import bisect
from collections import Counter
def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))


n, i = MI()
print(n-i+1)
