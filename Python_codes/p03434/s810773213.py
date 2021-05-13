from sys import stdin

n = stdin.readline().rstrip()
A = [int(x) for x in stdin.readline().rstrip().split()]

A.sort(reverse=True)

N=M=0

for i in range(0,len(A),2):
    N = N + A[i]

for i in range(1, len(A), 2):
    M = M + A[i]

print (N-M)





