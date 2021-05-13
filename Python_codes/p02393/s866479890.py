class itp1_2c:
    def sort(self,f,s,t):
        if(f>s):
            tmp=f
            f=s
            s=tmp
        if(s>t):
            tmp=s
            s=t
            t=tmp
        if(f>s):
            tmp=f
            f=s
            s=tmp
        print(str(f)+" "+str(s)+" "+str(t))     
if __name__=="__main__":
    num=map(int,raw_input().split(" "))
    run=itp1_2c()
    run.sort(num[0],num[1],num[2])