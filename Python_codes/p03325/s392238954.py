from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))
    cnt=0
    for i in range(n):
        while a[i]%2==0:
            a[i]//=2
            cnt+=1
    
    print(cnt)

if __name__=="__main__":
    main()