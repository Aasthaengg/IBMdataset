while True:
        k=map(int,raw_input().split())
        H=k[0]
        W=k[1]
        if H+W==0:
                break
#       
        if W%2==0:
                pattern="even"
        else:
                pattern="odd"
#
        if pattern=="even":
                f_line="#."*(W/2)
                s_line=".#"*(W/2)
        if pattern=="odd":
                f_line="#."*((W-1)/2)+"#"
                s_line=".#"*((W-1)/2)+"."
        for i in range(H):
                if i%2==0:
                        print f_line
                else:
                        print s_line
#
        print ""