class itp1_6a:
    def reverse(self,n,a):
        s=""
        for i in range(1,n+1):
            if i==n:
                s+=str(a[-1*i])
            else:
                s+=str(a[-1*i])+" "
        print s
if __name__=="__main__":
    n=input()
    a=map(int,raw_input().split(" "))
    run=itp1_6a()
    run.reverse(n,a)