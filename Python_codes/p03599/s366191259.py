def main():
    a,b,c,d,e,f = map(int,input().split())
    ans = []
    for i in range(f//a//100+1):
        for j in range((f-100*a*i)//b//100+1):
            if a*i*100+b*j*100 < f:
                ans.append([i,j])
    ans = ans[1:]
    D = 0
    A = [0,0]
    for an in ans:
        m = a*100*an[0] + b*100*an[1]
        slv = e*m//100
        M = 0
        for i in range(min(f-m,slv)//c+1):
            for j in range((min(f-m,slv)-c*i)//d+1):
                if i*c+d*j <= min(slv,f-m):
                    if M < i*c+d*j:
                        M = i*c+d*j
        den = M/(m+M)
        if den>=D:
            D = den
            A = [m+M,M]
    print(' '.join([str(a) for a in A]))

if __name__ == "__main__":
    main()