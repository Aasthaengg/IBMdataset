N = int(input())
A = list(map(int,input().split()))
Aall = A[0]
for i in range(1,N):
    Aall ^= A[i]
import sys
flag = True
for i in range(N):
    if A[i]^Aall != A[i]:
        flag = False
        print("No")
        sys.exit()
if flag:
    print("Yes")