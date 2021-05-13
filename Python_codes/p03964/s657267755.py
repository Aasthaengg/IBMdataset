import math
n = int(input())
T = [0]*n
A = [0]*n
for i in range(n):
    T[i], A[i] = map(int,input().split())

a = 1
b = 1
for ti, ai in zip(T,A):
    #n = max(math.ceil(a/ti),math.ceil(b/ai))
    n = max((a+ti-1)//ti,(b+ai-1)//ai)
    a = n*ti
    b = n*ai
    #print(a,b)
print(a+b)