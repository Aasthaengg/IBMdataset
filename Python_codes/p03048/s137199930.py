def main():
    r,g,b,n = map(int,input().split())
    c = 0
    for i in range(n//r+1):
        m = n - r * i
        for j in range(m//g+1):
            l = m - g * j
            if l % b == 0:
                c += 1
            
    print(c)

main()