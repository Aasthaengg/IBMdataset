while True:
        k=map(int,raw_input().split())
        H=k[0]
        W=k[1]
        if H+W==0:
                break
        else:
                print '#'*W
                if H==1:
                        break
                if H==2:
                        print '#'*W
                if H>2:
                        for i in range(H-2):
                                print '#'+ '.'*(W-2)+'#'
                        print '#'*W
        print ""