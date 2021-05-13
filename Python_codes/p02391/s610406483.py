class itp1_2a:
    def out(self,a,b):
        if a<b:
            print "a < b"
        elif a>b:
            print "a > b"
        else :
            print "a == b"
if __name__=="__main__":
    ipt=map(int,raw_input().split(" "))
    run=itp1_2a()
    run.out(ipt[0],ipt[1])