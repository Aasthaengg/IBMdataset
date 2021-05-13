from sys import stdin
def main():
    #入力
    readline=stdin.readline
    x=int(readline())

    n=x//11
    m=x%11
    if m==0: print(2*n)
    elif 1<=m<=6: print(2*n+1)
    else: print(2*n+2)

if __name__=="__main__":
    main()