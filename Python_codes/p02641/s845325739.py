import math , sys

X , N = list(map(int, input().split()))

A = list(map(int, input().split()))

F = math.inf
ans = math.inf
B  =[]
for i in range( -2 , 102):
    if i not in A:
        B.append(i)
#print(A,B)
for i in range(len(B)):
    d = abs( X - B[i] )
    #print(B[i] , d)
    if d < F:
        F = d
        ans = B[i]
    elif d==F:
        if B[i] < ans:
            ans = B[i]
print(ans)