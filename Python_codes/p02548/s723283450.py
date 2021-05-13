from sys import stdin
input = stdin.buffer.readline

N = int(input())
tmp = 0

for a in range(1,N):
    tmp = tmp + (N-1) // a
    
print(tmp)