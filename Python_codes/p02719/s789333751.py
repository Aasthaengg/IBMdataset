def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for _ in range(n)]
import math

n,k = L()
print(min((-n)%k,n%k))