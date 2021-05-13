from sys import stdin,stdout

if __name__=="__main__":
    n=int(stdin.readline())

    a=[int(x) for x in stdin.readline().split()]
    b=[int(x) for x in stdin.readline().split()]

    sm=0

    for i in range(n):
        if(a[i]>b[i]):
            sm+=a[i]-b[i]

    stdout.write(str(sm)+"\n")
