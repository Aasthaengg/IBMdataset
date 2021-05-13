from sys import stdin
def main():
    #入力
    readline=stdin.readline
    h1,m1,h2,m2,k=map(int,readline().split())
    print(max(0,(h2-h1)*60+(m2-m1)-k))
    
if __name__=="__main__":
    main()