import collections
def main():
    n = int(input())
    a=[int(i) for i in input().split()]
    res = []
    mina = min(a)
    maxa = max(a)
    min_ind,max_ind=0,0
    for i in range(n):
        if(a[i]==mina):
            min_ind = i+1
        if(a[i]==maxa):
            max_ind = i+1

    if(mina>=0):
        print(n-1)
        for i in range(n-1):
            print(i+1,i+2)
    elif(maxa<=0):
        print(n-1)
        for i in range(n-1):
            print(n-i,n-i-1)
    else:
        if(abs(mina)<=abs(maxa)):
            print(2*n-1)
            for i in range(n):
                print(max_ind,i+1)
            for i in range(n-1):
                print(i+1,i+2)
        else:
            print(2*n - 1)
            for i in range(n):
                print(min_ind,i+1)
            for i in range(n-1):
                print(n-i,n-i-1)

if __name__ == '__main__':
    main()
