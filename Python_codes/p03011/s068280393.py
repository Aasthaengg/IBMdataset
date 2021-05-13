from sys import stdin
def main():
    #入力
    readline=stdin.readline
    p,q,r=map(int,readline().split())
    print(min(p+q,q+r,r+p))
    
if __name__=="__main__":
    main()