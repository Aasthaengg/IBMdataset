def main():
    import math
    a,b = map(int,input().split())
    g = math.gcd(a,b)
    ans = [1]
    for m in range(2,int(g**0.5)+1):
        if g%m==0:
            ans.append(m)
            while g%m==0:
                g = g//m
        if g==1:
            break
    if g!=1:
        ans.append(g)
    print(len(ans))

if __name__ == "__main__":
    main()
