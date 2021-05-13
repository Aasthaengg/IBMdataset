n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i]//2
    
# print(a)
def calc(n):
    ret = 0
    while n%2 == 0:
        ret +=1
        n//=2
    return ret


flag = True
t = 0
for i in range(n-1):
    t = 2**calc(a[i])
    if calc(a[i]) == calc(a[i+1]):
        # print(calc(a[i]),calc(a[i+1]))
        continue
    else:
        flag = False
        break


def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)



if flag:
    lcm = 1
    for i in range(n):
        p = max(lcm, a[i])
        q = min(lcm, a[i])
        lcm = lcm*a[i]//gcd(p, q)
        # print(lcm)
    if (m//lcm)%2 == 0:
        print(int((m//lcm)//2))
    else:
        print(int((m//lcm+1)//2))

else:
    print(0)
