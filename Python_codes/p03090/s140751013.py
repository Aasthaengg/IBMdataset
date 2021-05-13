import sys
input = sys.stdin.readline

N = int(input())

S = N if N&1 else N+1
E = [(x,y) for x in range(1,N+1) for y in range(x+1,N+1) if x+y != S]

print(len(E))
for x,y in E:
    print(x,y)