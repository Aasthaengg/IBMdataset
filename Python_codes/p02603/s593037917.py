import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

money = 1000
stock = 0

def is_minimal(idx):
    if idx!=N-1:
        if A[idx+1]>A[idx]:
            return True
        else:
            return False

def is_maximal(idx):
    if idx!=N-1:
        if A[idx+1]<A[idx]:
            return True
        else:
            return False

for i in range(N-1):
    if is_minimal(i):
        stock += money//A[i]
        money %= A[i]
    elif is_maximal(i):
        money += A[i]*stock
        stock = 0

money += A[N-1]*stock
stock = 0
print(money)
    
