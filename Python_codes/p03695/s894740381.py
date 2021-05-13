from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    flags=[False]*8
    free=0
    for i in range(n):
        if a[i]//400<=7:
            flags[a[i]//400]=1
        else:
            free+=1

    color_max=flags.count(1)+free
    color_min=max(1,flags.count(1))
    print(color_min,color_max)

if __name__=="__main__":
    main()