import math
A,B,H,M=list(map(int, input().split()))


def getdegree(n,m):
    degm=m*6
    degn=(n%12)*30 + 0.5*m
    return min(abs(degn-degm), 360-abs(degn-degm))

D=math.radians(getdegree(H,M))
# print(D)
print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(D)))