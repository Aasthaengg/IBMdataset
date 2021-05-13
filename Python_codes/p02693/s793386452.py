import math
K = int(input())
A,B = map(int,input().split())

if K == 1:
    print("OK")
    exit()
if A%K==0:
    print("OK")
    exit()

x = math.floor(A/K)
y = math.floor(B/K)

if y-x > 0:
    print("OK")
else:
    print("NG")