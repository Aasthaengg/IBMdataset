def abc061_c():
    s = str(input())

    l = []
    def saiki(i,moji):
        if i == len(s)-1:
            #print(moji)
            l.append(sum(list(map(int,moji.split("+")))))
            return

        #いれる
        saiki(i+1,moji+"+"+s[i+1])
        #いれない
        saiki(i+1,moji+s[i+1])

    saiki(0,s[0])

    print(sum(l))


abc061_c()