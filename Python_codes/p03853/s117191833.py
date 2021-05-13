import sys

input = sys.stdin.readline
MOD = 1000000007

H,W = map(int,input().split())

c = []

for i in range(H):
    x = input()[:-1]
    c.append(x)
    

for i in range(2*H):
    print(c[i//2])
