import statistics
import math

N = int(input())
a = []
b = []
for i in range(N):
    A, B = map(int,input().split())
    a.append(A)
    b.append(B)

if N%2 == 1:
    ans = statistics.median(b) - statistics.median(a) + 1
else:
    ans = (statistics.median(b) - statistics.median(a))*2 + 1
print(int(ans))