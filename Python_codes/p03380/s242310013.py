from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    a.sort()
    a_max=a[-1]
    b_max=-1
    for i in range(n-1):
        if b_max<min(a[i],a_max-a[i]):
            b_max=a[i]

    print(a_max,b_max)

if __name__=="__main__":
    main()