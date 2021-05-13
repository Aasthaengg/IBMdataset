A,B,C,D=map(int,input().split())
#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

lcm_=lcm(C,D)
answer=B-A+1-(B//C-A//C)-(B//D-A//D)+(B//lcm_-A//lcm_)
if A%C==0:
    answer-=1
if A%D==0:
    answer-=1
if answer<=-1:
    print(0)
else:
    if A%C==0 and A%D==0:
        print(answer+1)
    else:
        print(answer)
