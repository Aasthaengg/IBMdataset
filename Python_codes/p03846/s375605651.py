# coding: utf-8
# Your code here!
import collections
N = int(input())
A = list(map(int,input().split()))
A.sort()
mod = 10 ** 9 + 7
Flg = True
if N % 2 == 1:
    a = A.pop(0)
    if a != 0:
        Flg = False

k = (N % 2) + 1
for i in range(N //2):
    if A[i *2] != k or A[i * 2 + 1] != k:
        Flg = False
    k += 2
    
if Flg:
    ans = (2 ** (N // 2)) % mod
else:
    ans = 0
    
print(ans)