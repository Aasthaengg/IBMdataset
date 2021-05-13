n, x, t = input().split()
N = int(n)
X = int(x)
T = int(t)
if N % X == 0:
    c = N / X
else:
    c = int(N / X) + 1 
C = int(c)
print(C*T)
