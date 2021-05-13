
def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

def f(tmp):
    tmp.sort(reverse=True)
    result=[]
    for i in tmp[1:]:
        if tmp[0]%i == 0:
            tmp.remove(i)
    for i in range(1,len(tmp)):
        result.append(lcm(tmp[0],tmp[i]))
    else:
        if result:
            return result
        else:
            return tmp
if __name__ == "__main__":
    n=int(input())
    t=[]
    for _ in range(n):
        t.append(int(input()))
    t.sort(reverse=True)
    if len(t)<2:
        print(t[0])
        exit(0)
    tmp=[]
    for i in range(1,n):
        tmp.append(lcm(t[0],t[i]))
    while len(tmp) > 1:
        tmp=f(tmp)
    if tmp[0] >1000000000000000000:
        print(1000000000000000000)
    else:
        print(tmp[0])
