import fractions

a,b,c,d=map(int,input().split())
def cal(x,div1,div2):
    ret1=x//div1
    ret2=x//div2
    ret3=x//int(((div1*div2)/fractions.gcd(div1,div2)))
    return x-(ret1+ret2-ret3)
print(cal(b,c,d)-cal(a-1,c,d))
