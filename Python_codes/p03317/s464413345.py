import sys,math
input = sys.stdin.readline

N,K=list(map(int,input().split()))
A = list(map(int,input().split()))

print(1+math.ceil((N-K)/(K-1)))
