#coding: UTF-8
import math

A, B, DEGREE = list(map(int, input().split()))
RADIAN = math.radians(DEGREE)

C = math.sqrt(A*A+B*B-2*A*B*math.cos(RADIAN))
S =A*B*math.sin(RADIAN)/2.0
H = 2*S/A

print("%.10f %.10f %.10f"%(S, A+B+C, H))
