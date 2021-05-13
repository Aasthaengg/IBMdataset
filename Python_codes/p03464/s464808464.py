import sys

K=int(input())
A=list(map(int,input().split()))
import math


MIN=2
MAX=2

for a in A[::-1]:
    M1=math.ceil(MIN/a)*a
    M2=MAX//a*a

    if M1>MAX:
        print(-1)
        sys.exit()

    else:
        MIN=M1
        MAX=M2+a-1

print(MIN,MAX)