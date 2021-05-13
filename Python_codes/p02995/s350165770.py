a,b,c,d = map(int,input().split())
import math
g = c*d//math.gcd(c,d)

num1=b//c
num2=b//d
num3=b//g
num4=(a-1)//c
num5=(a-1)//d
num6=(a-1)//g


print(b-a+1-(num1+num2-num3-num4-num5+num6))
