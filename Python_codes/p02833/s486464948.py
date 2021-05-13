from sys import stdin
from sys import exit
def main():
    #入力
    readline=stdin.readline
    n=int(readline())

    if n%2==1:
        print(0)
        exit()
    
    n//=2
    ans=0
    x=5
    while n//x>=1:
        ans+=n//x
        x*=5

    print(ans)

if __name__=="__main__":
    main()