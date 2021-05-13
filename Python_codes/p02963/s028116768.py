import sys
input = sys.stdin.readline

S = int(input())

M = 10 ** 9
t = (-S) % M
x = (S + t) // M

answer = [0,0,1,x,M,t]

print(*answer)
