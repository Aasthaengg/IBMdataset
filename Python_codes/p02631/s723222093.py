from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
xor=A[0]

for t in range(1,N):
    xor=xor^A[t]

for u in A:
    print(xor^u,end=' ')