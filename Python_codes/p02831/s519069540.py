a,b=map(int,input().split())

def lcm(a,b):#最小公倍数
    ori_a=a
    ori_b=b
    while b!=0:
        a,b=b,a%b
    return (ori_a*ori_b)//a

ans=lcm(a,b)
print(ans)