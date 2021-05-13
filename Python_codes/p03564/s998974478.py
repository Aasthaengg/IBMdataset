def main():
        n=int(input())
        k=int(input())
        a=1
        while(n>0):
            a=min(a+k,2*a)
            n-=1
        print(a)
main()