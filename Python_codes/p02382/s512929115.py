n = int(input())
xn = list(map(int, input().split()))
yn = list(map(int, input().split()))

Dp1, Dp2, Dp3, Dpinf = [0.0]*4

for (x, y) in zip(xn, yn):
    a = abs(x-y)
    Dp1 += a
    Dp2 += a**2
    Dp3 += a**3
    Dpinf = a if a > Dpinf else Dpinf

Dp2 = Dp2**(1/2)
Dp3 = Dp3**(1/3)

print(Dp1, Dp2, Dp3, Dpinf, sep='\n')