def gcd(a,b):
    if(a%b!=0):
        return gcd(b,a%b)
    else:
        return b
def lcm(a,b):
    return (a*b//(gcd(a,b)))
def main3():
    n,m=map(int, input().split())
    s=input()
    t=input()
    if(n>m):
        s1 = t
        t1 = s
    else:
        s1 = s
        t1 = t
    l = (lcm(n,m))
    l_n = l//n
    l_m = l//m
    i = 0
    ind_min = []
    ind_max = []
    while(i<min(n,m)):
        ind_min.append(i*max(l_n,l_m)+1)
        i+=1
    i = 0
    while(i<max(n,m)):
        ind_max.append(i*min(l_n,l_m)+1)
        i+=1

    ind_max_d = {k:i for i,k in enumerate(ind_max)}

    for i in range(len(ind_min)):
        if(ind_min[i] in ind_max_d):
            if(s1[i] != t1[ind_max_d[ind_min[i]]]):
                print(-1)
                exit()
    print(l)



if __name__ == '__main__':
    main3()
