import math
N = int(input())

ans = []
d = 40

t = 0
while d >= 0:
    bottom = t+(-2)**d+(-2)*(1-4**(d//2))//(-3)
    top = t+(-2)**d+(1-4**math.ceil(d/2))//(-3)
    if bottom <= N <= top:
        ans.append('1')
        t += (-2)**d
    else:
        ans.append('0')
    d -= 1

print(int(''.join(ans)))
