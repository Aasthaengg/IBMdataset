def main():
    while True:
        try:
            a,b=(int(x) for x in input().split())
        except:
            break
        a1=a
        b1=b
        while b!=0:
            c=a%b
            a=b
            b=c
        print(a, a1*b1//a)

main()
