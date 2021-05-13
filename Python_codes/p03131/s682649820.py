from sys import stdin
def main():
    #入力
    readline=stdin.readline
    k,a,b=map(int,readline().split())
    cnt=1
    if a>=b-1:
        cnt+=k
    else:
        if k<a-1:
            cnt+=k
        else:
            cnt=a
            k-=a-1

            l=k//2
            m=k%2
            cnt+=(b-a)*l
            cnt+=m
    
    print(cnt)

if __name__=="__main__":
    main()