import math

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

A, B, C, D = map(int, input().split())

CD = int(C*D / gcd(C, D))

B_cnt = B//C + B//D - B//CD
A_cnt = (A-1)//C + (A-1)//D - (A-1)//CD

print((B-A+1) - (B_cnt - A_cnt))

