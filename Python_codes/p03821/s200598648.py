import sys
readline = sys.stdin.buffer.readline
N = int(readline())
A = []
B = []
for i in range(N):
    Ai,Bi = map(int,input().split())
    A.append(Ai)
    B.append(Bi)
button = 0
for i in range(N)[::-1]:
    button += (B[i]-A[i]-button)%B[i]
print(button)