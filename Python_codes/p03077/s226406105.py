N = int(input())
A = int(input())
B = int(input())
C  = int(input())
D = int(input())
E = int(input())

if(N%min(A,B,C,D,E)!=0):
    ans = N//min(A,B,C,D,E) + 5
else:
    ans = N//min(A,B,C,D,E) + 5 - 1


print(ans)