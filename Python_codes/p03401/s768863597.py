from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    A=list(map(int,readline().split()))

    A.insert(0,0)
    A.append(0)
    S=0
    l=[]
    for i in range(N+1):
        a=A[i+1]-A[i]
        S+=abs(a)

    for i in range(N):
        l1=A[i+1]-A[i]
        l2=A[i+2]-A[i]
        l3=A[i+2]-A[i+1]
        print(S-abs(abs(l2)-(abs(l3)+abs(l1))))
if __name__=="__main__":
    main()