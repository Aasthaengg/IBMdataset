n,m,d = map(int, input().split())
"""
n以下のm個の数列に対して
絶対値がd
"""

if d !=0:
    print((n-d)*2*(m-1)/(n**2))
else:
    print(n*(m-1)/(n**2))