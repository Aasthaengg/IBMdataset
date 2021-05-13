import fractions

def lcm(x,y):
    return (x*y) // fractions.gcd(x, y)
    
x, y = map(int, input().split())
s = input()
t = input()

lc = lcm(x,y)

s_l = lc//x
t_l = lc//y

for i in range(y):
    if i%s_l == 0:
        if t[i] == s[i*t_l//s_l]:
            continue
        else:
            print(-1)
            break
else:
    print(lc)

