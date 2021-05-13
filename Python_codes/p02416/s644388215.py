while 1:
        T=raw_input()
        if T=="0":
                break
        t=list(T)
        s=0
        for i in range(len(t)):
                s+=int(t[i])
        print s