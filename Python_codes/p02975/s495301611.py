from sys import stdin
from collections import Counter
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    a=list(map(int,readline().split()))

    c=Counter(a)
    c=sorted(c.items())
    if N%3!=0:  #Nが3の倍数じゃない時
        if len(c)==1 and c[0][0]==0:
            print("Yes")
        else:
            print("No")

    elif N%3==0:  #Nが3の倍数の時
        if len(c)==1 and c[0][0]==0:
            print("Yes")
        elif len(c)==2 and c[0][0]==0 and c[0][1]==N//3:
            print("Yes")
        elif len(c)==3 and c[0][1]==N//3 and c[1][1]==N//3 and c[2][1]==N//3 and c[0][0]^c[1][0]^c[2][0]==0:
            print("Yes")
        else:
            print("No")

if __name__=="__main__":
    main()