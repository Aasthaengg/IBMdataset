N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
MIN = min(A,B,C,D,E)
d,m = divmod(N,MIN)
if m == 0:
    d -= 1
print(5+d)