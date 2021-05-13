import math

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k = nm()
a = nl()

print(math.ceil((n-1)/(k-1)))