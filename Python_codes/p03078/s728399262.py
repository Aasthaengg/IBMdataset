from sys import stdin
def main():
    #入力
    readline=stdin.readline
    x,y,z,k=map(int,readline().split())
    a=list(map(int,readline().split()))
    b=list(map(int,readline().split()))
    c=list(map(int,readline().split()))

    d=list()
    for i in range(x):
        for j in range(y):
            d.append(a[i]+b[j])

    d.sort(reverse=True)
    if x*y>=k:
        d=d[:k]

    e=list()
    for i in range(len(d)):
        for j in range(z):
            e.append(d[i]+c[j])

    e.sort(reverse=True)
    for i in range(k):
        print(e[i])

if __name__=="__main__":
    main()