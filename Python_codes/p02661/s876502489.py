# coding: utf-8

N = int(input())
A = []
B = []

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N%2 == 1:
    low = A[N//2]
    high = B[N//2]
    ans = high - low + 1
else:
    low = (A[N//2-1]+A[N//2])/2
    high = (B[N//2-1]+B[N//2])/2
    ans = int((high - low + 1)*2-1)

print(ans)