import sys
input = sys.stdin.readline

a,b=list(map(int,input().split()))
n=b-a
print((n)*(n-1)//2-a)
