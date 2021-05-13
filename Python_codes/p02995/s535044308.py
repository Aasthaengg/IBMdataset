a,b,c,d=map(int, input().split())
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

ans_b=b-(b//c)-(b//d)+(b//(lcm(c,d)))
ans_a=a-(a//c)-(a//d)+(a//(lcm(c,d)))
ans=ans_b-ans_a

if a%c!=0 and a%d!=0:
    ans+=1
print(ans)