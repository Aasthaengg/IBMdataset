from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    for i in range(n):
        if i==0:
            t,a=map(int,readline().split())
        else:
            t_i,a_i=map(int,readline().split())
            tmp1=(t+t_i-1)//t_i
            tmp2=(a+a_i-1)//a_i
            x=max(tmp1,tmp2)
            t=t_i*x
            a=a_i*x
    
    print(a+t)

if __name__=="__main__":
    main()