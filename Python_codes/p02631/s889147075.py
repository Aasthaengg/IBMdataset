from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    b=[0]*n

    s_xor=0
    i_1=0
    i_2=0
    for j in range(n):
        if j==0:
            for _ in range(n-1):
                s_xor^=a[i_1]
                i_1+=1
            b[i_1]=s_xor
        else:
            s_xor^=a[i_2]
            i_2+=1
            i_2%=n

            s_xor^=a[i_1]
            i_1+=1
            i_1%=n
            b[i_1]=s_xor

    print(*b)

if __name__=="__main__":
    main()