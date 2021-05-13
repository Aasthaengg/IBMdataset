class itp1_2b:
    def out(self,a,b,c):
        if a<b and b<c:
            print "Yes"
        else :
            print "No"
if __name__=="__main__":
 ipt=map(int,raw_input().split(" "))
 run=itp1_2b()
 run.out(ipt[0],ipt[1],ipt[2])