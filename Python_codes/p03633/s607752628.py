
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))
# print('T:',T)

if N==1:
    f2 = T[0]

elif N==2:
    import math
    a,b = T[0], T[1]
    f=math.gcd(a,b)
    f2=a*b//f

else:
    import math
    a,b = T[0], T[1]
    f=math.gcd(a,b)
    f2=a*b//f
    for i in range(2,N):
        a,b=f2, T[i]
        f=math.gcd(a,b)
        f2=a*b//f

print(f2)
