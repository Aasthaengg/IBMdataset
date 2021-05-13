#Subscribers
N,A,B = map(int, input().split())
M = min(A,B)
m = A + B - N
if m < 0:
    m = 0
print(M,m)