def gcd(x,y):
    if x < y:
        x,y = y,x
        
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return (x*y)//gcd(x,y)

a,b,c,d = map(int,input().split())

al = b-a+1

cnt_c = b//c - (a-1)//c 

cnt_d = b//d - (a-1)//d 

cnt_t = b//lcm(c,d) - (a-1)//lcm(c,d) 

print(al - cnt_c - cnt_d + cnt_t)